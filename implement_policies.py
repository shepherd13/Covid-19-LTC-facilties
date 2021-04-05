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
			for person in range(self.matric[facility].n_residents):
				self.replace_dead_people(day, person, facility)
				if day > self.parameters['Policy Start Testing']:
					self.testing(day, person, facility)
				if self.matric[facility].people[person].get_disease_state(day) in [2,3,4]: #.get_valid_test_state(day) == 1:
					facility_positive_cases += 1

			# Permanent Staff members
			for person in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				self.replace_dead_people(day, person, facility)
				#self.replace_infected_staff(day, person, facility)
				if day > self.parameters['Policy Start Testing']:
					self.testing(day, person, facility)
				if self.matric[facility].people[person].get_disease_state(day) in [2,3,4]: #get_valid_test_state(day) == 1:
					facility_positive_cases += 1

			# Temporary Staff members(visiting the facility that "day")
			for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
				if (np.sum(self.matric[facility].daily_contacts[day%7][person]) > 0):
					self.replace_dead_people(day, person, facility)
					#self.replace_infected_staff(day, person, facility)
					if day > self.parameters['Policy Start Testing']:
						self.testing(day, person, facility)
					if self.matric[facility].people[person].get_disease_state(day) in [2,3,4]: #get_valid_test_state(day) == 1:
						facility_positive_cases += 1

			if facility_positive_cases/(self.matric[facility].n_residents+self.matric[facility].n_staff) > self.parameters['Quarantine Location Infecion Rate']:
				if facility not in self.network.isolated_facilities:
					self.network.isolate_facility(facility)
		

	def replace_dead_people(self, day, person, facility):
		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		if current_disease_state == -2 and self.matric[facility].people[person].get_disease_state(day-1) != -2:
			self.network.update_contacts_when_person_die(facility, person)

	#def replace_infected_staff(self, day, person, facility):
	#	current_test_state = self.matric[facility].people[person].test_state
	#	if current_test_state == 1:
	#		self.network.update_contacts_when_staff_infected(facility, person)

	def testing(self, day, person, facility):
		if day - self.matric[facility].people[person].last_tested > self.parameters['Test Frequency']:
			self.viral_testing(day, person, facility)
			self.matric[facility].people[person].last_tested = day

	# To add turnaround time we will need to save test_states daywise in an array
	def viral_testing(self, day, person, facility):
		cur_state = self.matric[facility].people[person].get_disease_state(day)
		if cur_state in [0,1]:
			self.matric[facility].people[person].test_state = random.choices([-1, 1], [1.0 - self.parameters['False Positive Rate'], self.parameters['False Positive Rate']])[0]

		elif cur_state in [2,3,4]:
			self.matric[facility].people[person].test_state = random.choices([-1, 1], [self.parameters['False Negative Rate'], 1.0 - self.parameters['False Negative Rate']])[0]



