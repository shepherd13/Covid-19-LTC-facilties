import random
import numpy as np

class Policies:
	def __init__(self, parameters, matric, network):
		self.parameters = parameters
		self.matric = matric
		self.network = network

	def implement_policies(self, day):
		for facility in range(len(self.matric)):
			facility_positive_cases = 0
			# Residents
			person = 0
			while person in range(self.matric[facility].n_residents + self.matric[facility].n_staff):
				self.matric[facility].people[person].update_quarantine_status()
				if self.matric[facility].people[person].class_name() == 'Staff':
					if self.matric[facility].people[person].quarantine_status == -1:
						self.replace_recovered_staff(person, facility)
					
				if (self.matric[facility].is_working(day%7, person)):		###########################################################################################################
					self.replace_dead_people(day, person, facility)			########### check out if we need to change something over here ####  dead People might not have connections
					if self.matric[facility].people[person].get_disease_state(day) > 0:
						self.matric[facility].infected = True

					## Testing and Quarantining People
					if day > self.parameters['Policy Start Testing']:
						self.testing(day, person, facility)
					if self.matric[facility].people[person].get_test_state(day) == 1: #get_disease_state(day) in [2,3,4]:
						facility_positive_cases += 1
						if self.matric[facility].people[person].class_name() == 'Resident':
							if self.matric[facility].people[person].quarantine_days == 0:		# First day of qurantine
								self.quarantine_infected_resident(person, facility)
						if self.matric[facility].people[person].class_name() == 'Staff':
							if self.matric[facility].people[person].quarantine_days == 0:		# First day of qurantine
								self.replace_infected_staff(person, facility)
				person += 1

			if facility_positive_cases > 0:
				if facility not in self.network.infected_facilities:
					## Masking Policy
					self.matric[facility].start_masking_policy = 1
					self.network.infected_facilities.add(facility)
					## Social Distancing
					self.network.social_distancing(facility)

			## Isolating Facility
			if (facility_positive_cases > self.parameters['Quarantine Location Infection Rate'] * (self.matric[facility].n_residents+self.matric[facility].n_staff)):
				if facility not in self.network.isolated_facilities:
					self.network.isolate_facility(day, facility)
					self.matric[facility].quarantined = True


	def replace_dead_people(self, day, person, facility):
		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		if current_disease_state == -2 and self.matric[facility].people[person].get_disease_state(day-1) != -2:
			self.network.update_interactions_when_person_dies(facility, person)

	###########################################
	##### Take care of infected fillers #######
	###########################################
	def replace_infected_staff(self, person, facility):
		if self.matric[facility].people[person].employment_type in [2,3]:
			self.matric[facility].people[person].disease_state = [0] * int(self.parameters['Days'])
			self.matric[facility].people[person].test_state = [0] * int(self.parameters['Days'])
			self.matric[facility].people[person].last_tested = -self.parameters['Test 2 Frequency']-1
			self.matric[facility].people[person].days_infected = 0
		else:
			self.matric[facility].people[person].set_quarantine_status(1)
			self.matric[facility].people[person].update_quarantine_location(facility)
			self.network.update_interactions_when_person_quarantines(facility, person)

	def quarantine_infected_resident(self, person, facility):
		self.matric[facility].people[person].set_quarantine_status(1)
		self.matric[facility].people[person].update_quarantine_location(facility)
		self.network.update_interactions_when_person_quarantines(facility, person)

	def replace_recovered_staff(self, person, facility):
		self.network.update_interactions_when_person_quarantine_ends(facility, person)

	def testing(self, day, person, facility):
		testing_parameters = self.matric[facility].people[person].get_testing_parameters()
		if day - self.matric[facility].people[person].last_tested > testing_parameters['Test Frequency']:
			if day + int(testing_parameters['Test Result turnaround time']) < self.parameters['Days']:
				self.viral_testing(day, person, facility, testing_parameters)
				self.matric[facility].people[person].last_tested = day

	# To add turnaround time we will need to save test_states daywise in an array
	def viral_testing(self, day, person, facility, testing_parameters):
		cur_state = self.matric[facility].people[person].get_disease_state(day)
		if cur_state in [0,1]:
			self.matric[facility].people[person].test_state[day+int(testing_parameters['Test Result turnaround time'])] = random.choices([-1, 1], [1.0 - testing_parameters['False Positive Rate'], testing_parameters['False Positive Rate']])[0]

		elif cur_state in [2,3,4]:
			self.matric[facility].people[person].test_state[day+int(testing_parameters['Test Result turnaround time'])] = random.choices([-1, 1], [testing_parameters['False Negative Rate'], 1.0 - testing_parameters['False Negative Rate']])[0]

