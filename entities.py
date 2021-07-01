import random
import numpy as np

class Facility:
	def __init__(self, parameters, people, n_p_staff, n_t_staff, facility_details):
		self.daily_contacts = [0]*7
		self.parameters = parameters
		self.people = people
		self.n_residents = facility_details['residents']
		self.n_staff = len(people) - facility_details['residents']
		self.n_p_staff = n_p_staff
		self.n_t_staff = n_t_staff
		self.facility_code = facility_details['facility_code']
		self.affiliation = facility_details['affiliation']
		self.facility_type = facility_details['facility_type']
		self.start_masking_policy = parameters['Policy Start Masking']
		self.quarantine_days = 0
		self.infected = False
		self.quarantined = False

	def set_daily_contacts(self, day, contact_pattern):
		self.daily_contacts[day] = contact_pattern

	def is_working(self, day, person):
		return True if np.sum(self.daily_contacts[day%7][person]) > 0 else False


class Person:
	def __init__(self, parameters):
		self.parameters = parameters
		self.disease_state = [0] * int(self.parameters['Days'])
		self.last_updated = -1
		self.test_state = [0] * int(self.parameters['Days'])
		self.last_tested = -self.parameters['Test 1 Frequency']-1
		self.days_infected = 0
		self.incub_end = random.choice([5,6,7])
		self.infection_end = 7.8
		self.transmission_start = self.incub_end - 2
		self.transmission_end = 10
		self.quarantine_days = 0
		self.quarantine_status = 0
		self.last_recorded = -1

	# def update_test_state(self, day):
	# 	if day < int(self.parameters['Days'])-1:
	# 		if self.test_state[day+1] == 0:
	# 			if (self.test_state[day] == 1) and (day - self.last_tested > 14):
	# 				self.test_state[day+1] = 0
	# 			elif (self.test_state[day] == -1) and (day - self.last_tested > self.parameters['Test Frequency']):
	# 				self.test_state[day+1] = 0
	# 			else:
	# 				self.test_state[day+1] = self.test_state[day]

	def get_test_state(self, day):
		return self.test_state[day]

	def set_quarantine_status(self, status):
		self.quarantine_status = status

	def update_quarantine_location(self, facility):
		self.qurantine_location = facility

	def update_disease_state(self, day, state):
		self.disease_state[day] = state

	def get_disease_state(self, day):
		return self.disease_state[day]

	def class_name(self):
		return self.__class__.__name__

class Resident(Person):
	def __init__(self, gender, parameters):
		self.gender = gender
		#self.ethnicity = ethnicity
		#self.occupancy = occupancy
		super().__init__(parameters)

	def get_testing_parameters(self):
		testing_parameters = {'Test Frequency': self.parameters['Test 1 Frequency'],
							  'Test Result turnaround time': self.parameters['Test 1 Result turnaround time'],
							  'False Positive Rate': self.parameters['Test 1 False Positive Rate'],
							  'False Negative Rate': self.parameters['Test 1 False Negative Rate']}
		return testing_parameters

	def update_quarantine_status(self):
		if self.quarantine_status == 1:
			self.quarantine_days += 1
			if self.quarantine_days == self.parameters['Resident Quarantine Days']:
				self.set_quarantine_status(-1)		## 0: Not Quarantined, 1 Currently Quarantined, -1 Quarantine Over
		elif self.quarantine_status == -1:
			self.quarantine_days = 0
			self.set_quarantine_status(0)


class Staff(Person):
	def __init__(self, employment_type, parameters, shared_facilities):
		self.employment_type = employment_type
		self.shared_facilities = shared_facilities
		super().__init__(parameters)

	def update_shared_facilities(self, facility):
		self.shared_facilities.append(facility)


	def get_testing_parameters(self):
		testing_parameters = {'Test Frequency': self.parameters['Test 2 Frequency'],
							  'Test Result turnaround time': self.parameters['Test 2 Result turnaround time'],
							  'False Positive Rate': self.parameters['Test 2 False Positive Rate'],
							  'False Negative Rate': self.parameters['Test 2 False Negative Rate']}
		return testing_parameters

	def update_quarantine_status(self):
		if self.quarantine_status == 1:
			self.quarantine_days += 1
			if self.quarantine_days == self.parameters['Staff Quarantine Days']:
				self.set_quarantine_status(-1)		## 0: Not Quarantined, 1 Currently Quarantined, -1 Quarantine Over
		elif self.quarantine_status == -1:
			self.quarantine_days = 0
			self.set_quarantine_status(0)