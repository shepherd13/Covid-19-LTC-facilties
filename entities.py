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

	def update_contacts_when_person_die(self, person_id):
		if person_id < self.n_residents:
			replacement_id = self.n_residents
		else:
			print("STAFF DIED")
			replacement_id = self.n_residents + self.n_staff

		for day in range(7):
			temp_matrix = np.insert(self.daily_contacts[day], replacement_id, np.zeros(self.daily_contacts[day].shape[0]), 1)
			temp_matrix = np.insert(temp_matrix, replacement_id, np.zeros(temp_matrix.shape[1]), 0)
			temp_matrix[[person_id, replacement_id]] = temp_matrix[[replacement_id, person_id]]
			temp_matrix[:,[person_id, replacement_id]] = temp_matrix[:,[replacement_id, person_id]]
			self.daily_contacts[day] = temp_matrix
		gender = random.choices([0, 1], [self.parameters['MALE_PERCENTAGE'], 1 - self.parameters['MALE_PERCENTAGE']])[0]    #Male = 0, Female = 1
		new_person = Resident(gender, self.parameters)
		self.people = np.insert(self.people, self.n_residents, new_person)
		self.n_residents += 1

class Person:
	def __init__(self, parameters):
		self.parameters = parameters
		self.disease_state = [0] * int(self.parameters['Days'])
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


