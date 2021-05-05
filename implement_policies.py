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
				if self.matric[facility].people[person].class_name() == 'Staff':
					self.matric[facility].people[person].update_quarantine_status()
					if self.matric[facility].people[person].quarantine_status == -1:
						self.replace_recovered_staff(day, person, facility)
				if self.matric[facility].people[person].class_name() == 'Resident':
					self.matric[facility].people[person].update_quarantine_status()
					if self.matric[facility].people[person].quarantine_status == -1:
						self.remove_resident_from_cohort(day,person,facility)
				if (self.matric[facility].is_working(day%7, person)):
					self.replace_dead_people(day, person, facility)
					if day > self.parameters['Policy Start Testing']:
						self.testing(day, person, facility)
					if self.matric[facility].people[person].get_test_state(day) == 1: #get_disease_state(day) in [2,3,4]:
						facility_positive_cases += 1
						if self.matric[facility].people[person].class_name() == 'Staff':
							if self.matric[facility].people[person].quarantine_days == 0:		# First day of qurantine
								self.replace_infected_staff(day, person, facility)
				person += 1

			if facility_positive_cases/(self.matric[facility].n_residents+self.matric[facility].n_staff) > self.parameters['Quarantine Location Infecion Rate']:
				if facility not in self.network.isolated_facilities:
					self.network.isolate_facility(day, facility)


	def replace_dead_people(self, day, person, facility):
		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		if current_disease_state == -2 and self.matric[facility].people[person].get_disease_state(day-1) != -2:
			self.network.update_interactions_when_person_dies(facility, person)

	###########################################
	##### Take care of infected fillers #######
	###########################################
	def replace_infected_staff(self, day, person, facility):
		if self.matric[facility].people[person].employment_type in [2,3,5]:
			self.matric[facility].people[person].disease_state = [0] * int(self.parameters['Days'])
			self.matric[facility].people[person].test_state = [0] * int(self.parameters['Days'])
			self.matric[facility].people[person].last_tested = -self.parameters['Test Frequency']-1
			self.matric[facility].people[person].days_infected = 0
		else:
			self.matric[facility].people[person].set_quarantine_status(1)
			self.matric[facility].people[person].update_qurantine_location(facility)
			self.network.update_interactions_when_person_quarantines(facility, person)

	def replace_recovered_staff(self, day, person, facility):
		self.network.update_interactions_when_person_quarantine_ends(facility, person)

	def testing(self, day, person, facility):
		if day - self.matric[facility].people[person].last_tested > self.parameters['Test Frequency']:
			if day + int(self.parameters['Test Result turnaround time']) < self.parameters['Days']:
				self.viral_testing(day, person, facility)
				self.matric[facility].people[person].last_tested = day

	# To add turnaround time we will need to save test_states daywise in an array
	def viral_testing(self, day, person, facility):
		cur_state = self.matric[facility].people[person].get_disease_state(day)
		if cur_state in [0,1]:
			self.matric[facility].people[person].test_state[day+int(self.parameters['Test Result turnaround time'])] = random.choices([-1, 1], [1.0 - self.parameters['False Positive Rate'], self.parameters['False Positive Rate']])[0]

		elif cur_state in [2,3,4]:
			self.matric[facility].people[person].test_state[day+int(self.parameters['Test Result turnaround time'])] = random.choices([-1, 1], [self.parameters['False Negative Rate'], 1.0 - self.parameters['False Negative Rate']])[0]

	def send_resident_to_cohort(self,day,person,facility):
		self.matric[facility].people[person].set_quarantine_status(1)
		self.matric[facility].people[person].update_qurantine_location(facility)
		self.network.update_interaction_when_resident_sent_to_cohort(facility, person)

	def remove_resident_from_cohort(self,day,person,facility):
		self.network.update_interaction_when_resident_removed_from_cohort(facility,person)