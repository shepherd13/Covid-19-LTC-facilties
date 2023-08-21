import numpy as np
import random
import math

class InfectionTransfer:
	def __init__(self, parameters, matric):
		self.parameters = parameters
		self.matric = matric
		self.daily_residents_infected = [0] * len(self.matric)
		self.daily_staff_infected = [0] * len(self.matric)

	def update_daily_infected(self, person_index, facility, day):
		if(person_index < self.matric[facility].n_residents):
			self.daily_residents_infected[facility] += 1
		else:
			self.daily_staff_infected[facility] += 1

class InitialInfection(InfectionTransfer):
	def transfer(self, day):
		total_infected = 0
		# Randomly select a facility where the infection starts
		while(total_infected < -1):
			seed_facility = random.choice(range(len(self.matric)))
			# Intialize the states to 0
			self.daily_residents_infected = [0] * len(self.matric)
			self.daily_staff_infected = [0] * len(self.matric)
			for facility in range(seed_facility, seed_facility+1):#range(len(self.matric)):
				for staff in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_staff):
					self.matric[facility].people[staff].disease_state = [0] * int(self.parameters['Days'])

			infection_rate = self.parameters['Initial Infection Rate']
			for facility in range(seed_facility, seed_facility+1):#range(len(self.matric)):
				for staff in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_p_staff):
					if self.matric[facility].people[staff].vaccinated == 0 and (random.choices([0, 1], [1-infection_rate, infection_rate])[0] == 1):
						self.matric[facility].people[staff].update_disease_state(day, 1)   # infected, incubating
						self.update_daily_infected(staff, facility,day)

				for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
					if (np.sum(self.matric[facility].daily_contacts[day%7][staff]) > 0):
						if self.matric[facility].people[staff].vaccinated == 0 and (random.choices([0, 1], [1-infection_rate, infection_rate])[0] == 1):
							self.matric[facility].people[staff].update_disease_state(day, 1)   # infected, incubating
							self.update_daily_infected(staff, facility, day)

			for facility in range(seed_facility, seed_facility+1):
				total_infected = self.daily_residents_infected[facility] + self.daily_staff_infected[facility]
		return [(self.daily_residents_infected, self.daily_staff_infected)]


class ProbabilityPerInteraction(InfectionTransfer):
	def transfer(self, day):
		self.daily_residents_infected = [0] * len(self.matric)
		self.daily_staff_infected = [0] * len(self.matric)
		for fac in range(len(self.matric)):
			for staff in range(self.matric[fac].n_residents, self.matric[fac].n_residents + self.matric[fac].n_staff):
				coords = self.matric[fac].daily_contacts[day%7][staff].nonzero()[0]
				data = self.matric[fac].daily_contacts[day%7][staff][coords]
				residents_interacted = [c for c in coords if self.matric[fac].people[c].class_name()=='Resident']
				staff_interacted = [c for c in coords if self.matric[fac].people[c].class_name()=='Staff']
				for resident_ in residents_interacted:
					for interaction in range(int(data[np.where(coords==resident_)[0][0]])):
						self.spread_per_interaction(staff, resident_, day, fac)

				for staff_ in staff_interacted:
					for interaction in range(int(data[np.where(coords==staff_)[0][0]])):
						self.spread_per_interaction(staff, staff_, day, fac)
		return [(self.daily_residents_infected, self.daily_staff_infected)]

	def spread_per_interaction(self, person_1, person_2, day, facility):
		infection_probability = (1 - self.parameters['Masking efficiency'] * self.matric[facility].start_masking_policy) * self.parameters['Probability of infection per infectious contact']
		person_1_disease_state = self.matric[facility].people[person_1].get_disease_state(day)
		person_2_disease_state = self.matric[facility].people[person_2].get_disease_state(day)
		person_1_vaccination_state = self.matric[facility].people[person_1].vaccinated
		person_2_vaccination_state = self.matric[facility].people[person_2].vaccinated

		if person_1_disease_state == 2 or person_1_disease_state == 3 or person_1_disease_state == 4:
			if person_2_disease_state == 0 and person_2_vaccination_state == 0 and (random.choices([0, 1], [1 - infection_probability, infection_probability])[0] == 1):
				self.matric[facility].people[person_2].update_disease_state(day, 1)   # infected, incubating
				self.update_daily_infected(person_2, facility, day)

		elif person_2_disease_state == 2 or person_2_disease_state == 3 or person_2_disease_state == 4:
			if person_1_disease_state == 0 and person_1_vaccination_state == 0 and (random.choices([0, 1], [1 - infection_probability, infection_probability])[0] == 1):
				self.matric[facility].people[person_1].update_disease_state(day, 1)   # infected, incubating
				self.update_daily_infected(person_1, facility, day)


class GroupAirborneTransmission(InfectionTransfer):
	def transfer(self, day):
		self.daily_residents_infected = [0] * len(self.matric)
		self.daily_staff_infected = [0] * len(self.matric)
		for fac in range(len(self.matric)):
			total_quanta = 0
			initially_infected = []
			for person in range(self.matric[fac].n_residents + self.matric[fac].n_staff):
				if self.matric[fac].is_working(day%7, person):
					if self.matric[fac].people[person].get_disease_state(day) in [2,3,4]:
						initially_infected.append(person)
						ratio = 1 - (self.parameters['Masking efficiency'] * self.matric[fac].start_masking_policy)
						total_quanta += self.parameters['Quanta Rate'] * ratio

			if total_quanta > 0:
				for person in range(self.matric[fac].n_residents + self.matric[fac].n_staff):
					if self.matric[fac].is_working(day%7, person):
						if self.matric[fac].people[person].get_disease_state(day) == 0:
							transmission_probability = self.wells_riley(total_quanta)
							if (random.choices([0, 1], [1.0 - transmission_probability, transmission_probability])[0] == 1):
								self.matric[fac].people[person].update_disease_state(day, 1)  # infected, incubating

		return [(self.daily_residents_infected, self.daily_staff_infected)]

	# returns probability of getting infected by airborne infection
	# pulmonary ventilation rate is in (m3/s)
	# quanta rate is in (quanta/h), hard to calculate
	# time is the number of hours
	# room ventilation rate is in (AC/h)
	# room volume is in (m3)
	def wells_riley(self, total_quanta):
		prob = 1.0 - math.exp(-(total_quanta * (self.parameters['Pulmonary ventilation rate']
				* (1.0 - self.parameters['Masking efficiency'])) * self.parameters['Social time spent'])
				/ (self.parameters['Ventilation Rate'] * self.parameters['Room volume']))
		return prob

class OutsideTransmission(InfectionTransfer):
	def transfer(self, day):
		self.daily_residents_infected = [0] * len(self.matric)
		self.daily_staff_infected = [0] * len(self.matric)
		infection_rate = self.parameters['Outside Transmission Rate']
		for facility in range(len(self.matric)):
			for staff in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				if (self.matric[facility].people[staff].vaccinated == 0 and self.matric[facility].people[staff].get_disease_state(day) == 0) and (random.choices([0, 1], [1-infection_rate, infection_rate])[0] == 1):
					self.matric[facility].people[staff].update_disease_state(day, 1)   # infected, incubating
					self.update_daily_infected(staff, facility, day)

			for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
				if (np.sum(self.matric[facility].daily_contacts[day % 7][staff]) > 0):
					if (self.matric[facility].people[staff].vaccinated == 0 and self.matric[facility].people[staff].get_disease_state(day) == 0) and (random.choices([0, 1], [1-infection_rate, infection_rate])[0] == 1):
						self.matric[facility].people[staff].update_disease_state(day, 1)   # infected, incubating
						self.update_daily_infected(staff, facility, day)
		return [(self.daily_residents_infected, self.daily_staff_infected)]
