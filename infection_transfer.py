import numpy as np
import random

class InfectionTransfer:
	daily_residents_infected = 0
	daily_staff_infected = 0
	def __init__(self, parameters, matric):
		self.parameters = parameters
		self.matric = matric

	def update_daily_infected(self, person_index, facility):
		if(person_index < self.matric[facility].n_residents):
			self.daily_residents_infected += 1
		else:
			self.daily_staff_infected += 1

class InitialInfection(InfectionTransfer):
	def transfer(self, day):
		infection_rate = self.parameters['Initial Infection Rate']
		for facility in range(len(self.matric)):
			for staff in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				if (random.choices([0, 1], [1-infection_rate, infection_rate])[0] == 1):
					self.matric[facility].people[staff].update_disease_state(day, 1)   # infected, incubating
					self.update_daily_infected(staff, facility)

		for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
			if (random.choices([0, 1], [1-infection_rate, infection_rate])[0] == 1):
				self.matric[facility].people[staff].update_disease_state(day, 1)   # infected, incubating
				self.update_daily_infected(staff, facility)
		return self.daily_residents_infected + self.daily_staff_infected


class ProbabilityPerInteraction(InfectionTransfer):
	def transfer(self, day):
		self.daily_residents_infected = 0
		self.daily_staff_infected = 0
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
		return self.daily_residents_infected + self.daily_staff_infected

	def spread_per_interaction(self, person_1, person_2, day, facility):
		infection_probability = self.parameters['Probability of infection per infectious contact']
		person_1_disease_state = self.matric[facility].people[person_1].get_disease_state(day)
		person_2_disease_state = self.matric[facility].people[person_2].get_disease_state(day)

		if person_1_disease_state == 2 or person_1_disease_state == 3 or person_1_disease_state == 4:
			if person_2_disease_state == 0 and (random.choices([0, 1], [1 - infection_probability, infection_probability])[0] == 1):
				self.matric[facility].people[person_2].update_disease_state(day, 1)   # infected, incubating
				self.update_daily_infected(person_2, facility)

		elif person_2_disease_state == 2 or person_2_disease_state == 3 or person_2_disease_state == 4:
			if person_1_disease_state == 0 and (random.choices([0, 1], [1 - infection_probability, infection_probability])[0] == 1):
				self.matric[facility].people[person_1].update_disease_state(day, 1)   # infected, incubating
				self.update_daily_infected(person_1, facility)


class OutsideTransmission(InfectionTransfer):
	def transfer(self, day, matric, disease_state):	
		transmission_rate_type = self.parameters['Transmission rate type']
		if transmission_rate_type == 'static':
			otr = self.parameters['Outside Transmission Rate'] * TOTAL_SUSCEPTIBLE_STAFF
			while(otr > 0):
				if otr > 1:
					staff = self.find_random_susceptible_person(day, disease_state)
					disease_state[day, staff] = 1   # infected, incubating
					self.update_daily_infected(staff)
				else:
					if (random.choices([0, 1], [1.0 - otr, otr])[0] == 1):
						staff = self.find_random_susceptible_person(day, disease_state)
						disease_state[day, staff] = 1   # infected, incubating
						#self.update_daily_infected(staff)
				otr -= 1
		return disease_state

	def find_random_susceptible_person(self, day, facility):
		while True:
			person = random.choice(range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_staff))
			if self.matric[facility].people[person].get_disease_state(day) == 0:
				return person