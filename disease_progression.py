import random

class DiseaseProgression:
	def __init__(self, parameters, matric):
		self.parameters = parameters
		self.matric = matric

class Covid19_DiseaseProgression(DiseaseProgression):
	# States: Dead(-2), Recovered (-1), Susceptible (0), Incubating (1), Transmiting (2), Symptomatic (3), Asymptomatic(4), Symptomatic Quarantined (5),
	# Asymptomatic Quarantined (6), Symptomatic Spreader (7)

	def update_states(self, day, person, facility):
		current_disease_state = self.matric[facility].people[person].get_disease_state(day)

		if current_disease_state > 0:
			self.matric[facility].people[person].days_infected += 1

			# incubating
			if current_disease_state == 1:
				if self.matric[facility].people[person].days_infected >= self.matric[facility].people[person].transmission_start:
					self.matric[facility].people[person].update_disease_state(day, 2)  # transmitting

				if self.matric[facility].people[person].transmission_start == self.matric[facility].people[person].incub_end:
					# roll if asymptomatic or symptomatic
					if (random.choices([0, 1], [self.parameters['Asymptomatic Rate'], 1.0 - self.parameters['Asymptomatic Rate']])[0] == 1):
						self.matric[facility].people[person].update_disease_state(day, 3)  # symptomatic
					else:
						self.matric[facility].people[person].update_disease_state(day, 4)  # asymptomatic

			# transmitting
			elif current_disease_state == 2:
				#if days_infected[person] >= incub_end[person]:
				if self.matric[facility].people[person].days_infected >= self.matric[facility].people[person].incub_end:
					self.matric[facility].people[person].infection_start = 1000
					if (random.choices([0, 1], [self.parameters['Asymptomatic Rate'], 1.0 - self.parameters['Asymptomatic Rate']])[0] == 1):
						self.matric[facility].people[person].update_disease_state(day, 3) # symptomatic
					else:
						self.matric[facility].people[person].update_disease_state(day, 4) # asymptomatic
				# if infection over
				if (self.matric[facility].people[person].days_infected - self.matric[facility].people[person].transmission_start) >= self.matric[facility].people[person].transmission_end:
					self.matric[facility].people[person].update_disease_state(day, -1)  # recovered

			# symptomatic
			elif current_disease_state == 3:
				# if infection over
				if (self.matric[facility].people[person].days_infected - self.matric[facility].people[person].transmission_start) >= self.matric[facility].people[person].transmission_end:
					self.matric[facility].people[person].update_disease_state(day, -1)  # recovered

			# asymptomatic
			elif current_disease_state == 4:
				# if infection over
				if (self.matric[facility].people[person].days_infected - self.matric[facility].people[person].transmission_start) >= self.matric[facility].people[person].transmission_end:
					self.matric[facility].people[person].update_disease_state(day, -1)  # recovered


	def disease_progression(self, day):
		for facility in range(len(self.matric)):
			for person in range(self.matric[facility].n_residents+self.matric[facility].n_p_staff):
				self.update_states(day, person, facility)

		for person in range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
			self.update_states(day, person, facility)




