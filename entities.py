import random
import numpy as np

class Facility:
	def __init__(self, parameters, people, n_p_staff, n_t_staff, n_residents, n_staff, zipcode, affiliation, facility_type):
		self.daily_contacts = [0]*7
		self.parameters = parameters
		self.people = people
		self.n_residents = n_residents
		self.n_staff = len(people) - n_residents
		self.n_p_staff = n_p_staff
		self.n_t_staff = n_t_staff
		self.zipcode = zipcode
		self.affiliation = affiliation
		self.facility_type = facility_type

	def set_daily_contacts(self, day, contact_pattern):
		self.daily_contacts[day] = contact_pattern


class Person:
	def __init__(self, parameters):
		self.parameters = parameters
		self.disease_state = [0] * int(self.parameters['Days'])
		self.test_state = [0] * int(self.parameters['Days'])
		self.last_tested = -parameters['Test Frequency']-1
		self.days_infected = 0
		self.incub_end = random.choice([5,6,7])
		self.infection_end = 7.8
		self.transmission_start = self.incub_end - 2
		self.transmission_end = 10

	def update_test_state(self, day):
		if day < int(self.parameters['Days'])-1:
			if self.test_state[day+1] == 0:
				self.test_state[day+1] = self.test_state[day]

	# def get_current_test_state(self, day):
	# 	if day - self.last_tested <= self.parameters['Test Frequency']:
	# 		return self.test_state[day]


	def get_valid_test_state(self, day):
		if self.test_state[day] == 1:
			if day - self.last_tested > self.parameters['Test Frequency']:
				self.test_state[day] = 0
				return self.test_state[day]
		elif self.test_state[day] == -1:
			if day - self.last_tested[day] > 14:
				self.test_state[day] = 0
				return self.test_state[day]
		return self.test_state[day]


	# def get_disease_state(day):
	#	return self.disease_state[day]

	def update_disease_state(self, day, state):
		self.disease_state[day] = state

	def get_disease_state(self, day):
		return self.disease_state[day]

	def update_days_infeted(self, day, state):
		self.disease_state[day] = state

	# def get_days_infected(self, day):
	# 	return self.days_infected

	def class_name(self):
		return self.__class__.__name__

class Resident(Person):
	def __init__(self, gender, parameters):
		self.gender = gender
		#self.ethnicity = ethnicity
		#self.occupancy = occupancy
		super().__init__(parameters)


class Staff(Person):
	def __init__(self, emplyment_type, parameters):
		self.emplyment_type = emplyment_type
		super().__init__(parameters)


