import random

class Facility:
	def __init__(self, people, n_p_staff, n_t_staff, n_residents, n_staff, zipcode, affiliation, facility_type):
		self.daily_contacts = [0]*7
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
	def __init__(self):
		self.disease_state = [0]
		self.days_infected = 0
		self.incub_end = random.choice([5,6,7])
		self.infection_end = 7.8
		self.transmission_start = self.incub_end - 2
		self.transmission_end = 10

	# def update_test_state(self, day, state):
	# 	self.test_state[day] = state

	# def get_test_state(self, day):
	# 	return self.test_state

	# def get_disease_state(day):
	#	return self.disease_state[day]

	def update_disease_state(self, day, state):
		self.disease_state[day] = state

	def update_next_days_disease_state(self, state):
		self.disease_state.append(state)

	def get_disease_state(self, day):
		return self.disease_state[day]

	def update_days_infeted(self, day, state):
		self.disease_state[day] = state

	# def get_days_infected(self, day):
	# 	return self.days_infected

	def class_name(self):
		return self.__class__.__name__

class Resident(Person):
	def __init__(self, gender):
		self.gender = gender
		#self.ethnicity = ethnicity
		#self.occupancy = occupancy
		super().__init__()


class Staff(Person):
	def __init__(self, emplyment_type):
		self.emplyment_type = emplyment_type
		super().__init__()


