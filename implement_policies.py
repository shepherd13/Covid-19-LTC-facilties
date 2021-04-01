import random
import numpy as np

class Policies:
	def __init__(self, parameters, matric, network):
		self.parameters = parameters
		self.matric = matric
		self.network = network

	def implement_policies(self,day):
		self.replace_dead_people(day)
		self.quarantine_facility(day)
		if day > self.parameters['Policy Start Testing']:
			self.testing(day)

	def replace_dead_people(self, day):
		for facility in range(len(self.matric)):
			for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				current_disease_state = self.matric[facility].people[person].get_disease_state(day)
				if current_disease_state == -2 and self.matric[facility].people[person].get_disease_state(day-1) != -2:
					self.network.update_contacts_when_person_die(facility, person)

		# for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
		# 		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		# 		self.record_states(day, current_disease_state)

	def quarantine_facility(self, day):
		for facility in range(len(self.matric)):
			if facility not in self.network.isolated_facilities:
				total_infected = 0
				for person in range(self.matric[facility].n_residents+self.matric[facility].n_p_staff):
					if self.matric[facility].people[person].get_valid_test_state(day) == 1:
						total_infected += 1

				for person in range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff):
					if (np.sum(self.matric[facility].daily_contacts[day%7][person]) > 0) and self.matric[facility].people[person].get_valid_test_state(day) == -1:
						total_infected += 1

				if total_infected/(self.matric[facility].n_residents+self.matric[facility].n_staff) > self.parameters['Quarantine Location Infecion Rate']:
					self.network.isolate_facility(facility)


	def testing(self, day):
		for facility in range(len(self.matric)):
			for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				if day - self.matric[facility].people[person].last_tested > self.parameters['Test Frequency']:
					self.viral_testing(day, person, facility)
					self.matric[facility].people[person].last_tested = day

		for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
			if day - self.matric[facility].people[person].last_tested > self.parameters['Test Frequency']:
				self.viral_testing(day, person, facility)

	def viral_testing(self, day, person, facility):
		cur_state = self.matric[facility].people[person].get_disease_state(day)
		if cur_state in [0,1]:
			self.matric[facility].people[person].test_state = random.choices([-1, 1], [1.0 - self.parameters['False Positive Rate'], self.parameters['False Positive Rate']])[0]

		elif cur_state in [2,3,4]:
			self.matric[facility].people[person].test_state = random.choices([-1, 1], [self.parameters['False Negative Rate'], 1.0 - self.parameters['False Negative Rate']])[0]