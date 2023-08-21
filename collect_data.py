import csv
import numpy as np

class Collect_data:
	def __init__(self, parameters, network, facility_wise=None):
		self.parameters = parameters
		self.days = int(self.parameters['Days'])
		self.matric = network.matric
		self.facility_wise = int(self.parameters['Collect_Data_Facilitywise'])
		if self.facility_wise == 0:
			self.susceptible = [0] * self.days
			self.infected = [0] * self.days
			self.cumulative_infected = [0] * self.days
			self.cumulative_infected_residents = [0] * self.days
			self.cumulative_infected_staff = [0] * self.days
			self.daily_infected = [0] * self.days
			self.daily_infected_residents = [0] * self.days
			self.daily_infected_staff = [0] * self.days
			self.incubating = [0] * self.days
			self.transmitting = [0] * self.days
			self.symptomatic = [0] * self.days
			self.asymptomatic = [0] * self.days
			self.recovered = [0] * self.days
			self.residents_recovered = [0] * self.days
			self.staff_recovered = [0] * self.days
			self.dead = [0] * self.days
			self.daily_tested = [0] * self.days
			self.daily_tested_positive = [0] * self.days
			self.daily_tested_negative = [0] * self.days
			self.cumulative_tested_positive = [0] * self.days
			self.quarantined = [0] * self.days
			self.infected_facilities = [0] * self.days
			self.quarantined_facilities = [0] * self.days
		else:
			self.susceptible = [([0] * self.days) for i in range(len(self.matric))]
			self.infected = [([0] * self.days) for i in range(len(self.matric))]
			self.cumulative_infected = [([0] * self.days) for i in range(len(self.matric))]
			self.cumulative_infected_residents = [([0] * self.days) for i in range(len(self.matric))]
			self.cumulative_infected_staff = [([0] * self.days) for i in range(len(self.matric))]
			self.daily_infected = [([0] * self.days) for i in range(len(self.matric))]
			self.daily_infected_residents = [([0] * self.days) for i in range(len(self.matric))]
			self.daily_infected_staff = [([0] * self.days) for i in range(len(self.matric))]
			self.incubating = [([0] * self.days) for i in range(len(self.matric))]
			self.transmitting = [([0] * self.days) for i in range(len(self.matric))]
			self.symptomatic = [([0] * self.days) for i in range(len(self.matric))]
			self.asymptomatic = [([0] * self.days) for i in range(len(self.matric))]
			self.recovered = [([0] * self.days) for i in range(len(self.matric))]
			self.residents_recovered = [([0] * self.days) for i in range(len(self.matric))]
			self.staff_recovered = [([0] * self.days) for i in range(len(self.matric))]
			self.dead = [([0] * self.days) for i in range(len(self.matric))]
			self.daily_tested = [([0] * self.days) for i in range(len(self.matric))]
			self.daily_tested_positive = [([0] * self.days) for i in range(len(self.matric))]
			self.daily_tested_negative = [([0] * self.days) for i in range(len(self.matric))]
			self.cumulative_tested_positive = [([0] * self.days) for i in range(len(self.matric))]
			self.quarantined = [([0] * self.days) for i in range(len(self.matric))]
			self.infected_facilities = [([0] * self.days) for i in range(len(self.matric))]
			self.quarantined_facilities = [([0] * self.days) for i in range(len(self.matric))]

	def record_states(self, day, person, facility):
		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		current_test_state = self.matric[facility].people[person].get_test_state(day)

		if self.facility_wise == 0:
			# Based on Disease states
			if(current_disease_state == 0):
				self.susceptible[day] += 1

			elif(current_disease_state == 1):
				self.incubating[day] += 1
				self.infected[day] += 1          

			elif(current_disease_state == 2):
				self.transmitting[day] += 1 
				self.infected[day] += 1

			elif(current_disease_state == 3):
				#self.transmitting[day] += 1
				self.symptomatic[day] += 1
				self.infected[day] += 1

			elif(current_disease_state == 4):
				#self.transmitting[day] += 1
				self.asymptomatic[day] += 1
				self.infected[day] += 1

			elif(current_disease_state == -1):
				if self.matric[facility].people[person].get_disease_state(day-1) != -1:
					if self.matric[facility].people[person].class_name() == 'Resident':
						self.residents_recovered[day] += 1
					else:
						self.staff_recovered[day] += 1
					self.recovered[day] += 1

			elif(current_disease_state == -2):
				self.dead[day] += 1

			# Based on Test states
			if(current_test_state == 1):
				self.daily_tested_positive[day] += 1
			elif(current_test_state == -1):
				self.daily_tested_negative[day] += 1

			if self.matric[facility].people[person].last_tested == day:
				self.daily_tested[day] += 1

			if self.matric[facility].people[person].quarantine_status == 1:
				self.quarantined[day] += 1


		else:
			# Based on Disease states
			if(current_disease_state == 0):
				self.susceptible[facility][day] += 1

			elif(current_disease_state == 1):
				self.incubating[facility][day] += 1
				self.infected[facility][day] += 1          

			elif(current_disease_state == 2):
				self.transmitting[facility][day] += 1
				self.infected[facility][day] += 1

			elif(current_disease_state == 3):
				#self.transmitting[facility][day] += 1
				self.symptomatic[facility][day] += 1
				self.infected[facility][day] += 1

			elif(current_disease_state == 4):
				#self.transmitting[facility][day] += 1
				self.asymptomatic[facility][day] += 1
				self.infected[facility][day] += 1

			elif(current_disease_state == -1):
				if self.matric[facility].people[person].get_disease_state(day-1) != -1:
					if self.matric[facility].people[person].class_name() == 'Resident':
						self.residents_recovered[facility][day] += 1
					else:
						self.staff_recovered[facility][day] += 1
					self.recovered[facility][day] += 1

			elif(current_disease_state == -2):
				self.dead[facility][day] += 1

			# Based on Test states
			if(current_test_state == 1):
				self.daily_tested_positive[facility][day] += 1
			elif(current_test_state == -1):
				self.daily_tested_negative[facility][day] += 1

			if self.matric[facility].people[person].last_tested == day:
				self.daily_tested[facility][day] += 1

			if self.matric[facility].people[person].quarantine_status == 1:
				self.quarantined[facility][day] += 1

	def update_states(self, day, daily_infected):
		if self.facility_wise == 0:
			self.infected_facilities[day] = []
			for facility in range(len(self.matric)):
				indicies = list(range(self.matric[facility].n_residents + self.matric[facility].n_p_staff))
				self.set_states(day, facility, indicies)

				indicies = list(range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff))
				self.set_states(day, facility, indicies)

				if self.matric[facility].infected:
					self.infected_facilities[day].append(facility)
					#self.infected_facilities[day] += 1

				if self.matric[facility].quarantined:
					self.quarantined_facilities[day] += 1

			# Disease States
			self.daily_infected[day] = np.sum(daily_infected)
			self.daily_infected_residents[day] = np.sum([di[0] for di in daily_infected])
			self.daily_infected_staff[day] = np.sum([di[1] for di in daily_infected])

			self.cumulative_infected[day] = np.sum(daily_infected)
			self.cumulative_infected_residents[day] = np.sum([di[0] for di in daily_infected])
			self.cumulative_infected_staff[day] = np.sum([di[1] for di in daily_infected])
			if day > 0:
				self.cumulative_infected[day] += self.cumulative_infected[day-1]
				self.cumulative_infected_residents[day] += self.cumulative_infected_residents[day-1]
				self.cumulative_infected_staff[day] += self.cumulative_infected_staff[day-1]
				self.recovered[day] += self.recovered[day-1]
				self.residents_recovered[day] += self.residents_recovered[day-1]
				self.staff_recovered[day] += self.staff_recovered[day-1]

			# Test States
			self.cumulative_tested_positive[day] = self.daily_tested_positive[day]
			if day > 0:
				self.cumulative_tested_positive[day] += self.cumulative_tested_positive[day-1]

		else:
			for facility in range(len(self.matric)):
				indicies = list(range(self.matric[facility].n_residents + self.matric[facility].n_p_staff))
				self.set_states(day, facility, indicies)

				# temp staff who are visiting the facility that day
				indicies = self.matric[facility].daily_contacts[day%7].sum(0)[self.matric[facility].n_residents+self.matric[facility].n_p_staff : self.matric[facility].n_residents+self.matric[facility].n_staff]
				indicies = [i+self.matric[facility].n_residents+self.matric[facility].n_p_staff for i in indicies.nonzero()[0]]
				self.set_states(day, facility, indicies)

				if self.matric[facility].infected:
					self.infected_facilities[facility][day] += 1

				if self.matric[facility].quarantined:
					self.quarantined_facilities[facility][day] += 1

				## Specifically set states of Quarantined temporary staff
				indicies = []
				for person in range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff):
					if (self.matric[facility].people[person].quarantine_days > 0) and (self.matric[facility].people[person].qurantine_location == facility):
						indicies.append(person)
				self.set_states(day, facility, indicies)


				# Disease States
				self.daily_infected[facility][day] = np.sum([di for model in daily_infected for di in model], 0)[facility]
				self.daily_infected_residents[facility][day] = np.sum([di[0] for di in daily_infected], 0)[facility]
				self.daily_infected_staff[facility][day] = np.sum([di[1] for di in daily_infected], 0)[facility]

				self.cumulative_infected[facility][day] = np.sum([di for model in daily_infected for di in model], 0)[facility]
				self.cumulative_infected_residents[facility][day] = np.sum([di[0] for di in daily_infected], 0)[facility]
				self.cumulative_infected_staff[facility][day] = np.sum([di[1] for di in daily_infected], 0)[facility]
				if day > 0:
					self.cumulative_infected[facility][day] += self.cumulative_infected[facility][day-1]
					self.cumulative_infected_residents[facility][day] += self.cumulative_infected_residents[facility][day-1]
					self.cumulative_infected_staff[facility][day] += self.cumulative_infected_staff[facility][day-1]
					self.recovered[facility][day] += self.recovered[facility][day-1]
					self.residents_recovered[facility][day] += self.residents_recovered[facility][day-1]
					self.staff_recovered[facility][day] += self.staff_recovered[facility][day-1]

				# Test States
				self.cumulative_tested_positive[facility][day] = self.daily_tested_positive[facility][day]
				if day > 0:
					self.cumulative_tested_positive[facility][day] += self.cumulative_tested_positive[facility][day-1]


	def set_states(self, day, facility, indicies):
		for person in indicies:
			# self.matric[facility].people[person].update_test_state(day)
			if self.matric[facility].people[person].last_recorded != day:
				current_disease_state = self.matric[facility].people[person].get_disease_state(day)
				self.record_states(day, person, facility)
				# set states for next day
				if (day + 1) != self.days:
					self.matric[facility].people[person].update_disease_state(day + 1, current_disease_state)
				self.matric[facility].people[person].last_recorded = day


	def update_csv(self, export_file):
		if self.facility_wise == 0:
			with open(self.parameters['Output Directory'] + export_file, 'w', newline = '') as g:
				writer = csv.writer(g)
				l = []
				writer.writerow(l)

				l = []
				l.append('Day')
				l.append('Susceptible')
				l.append('Infected')
				l.append('Cumulative Infected')
				l.append('Cumulative Infected Residents')
				l.append('Cumulative Infected Staff')
				l.append('Daily Infected')
				l.append('Daily Infected Residents')
				l.append('Daily Infected Staff')
				l.append('Incubating')
				l.append('Transmitting')
				l.append('Symptomatic')
				l.append('Asymptomatic')
				l.append('Recovered')
				l.append('Residents Recovered')
				l.append('Staff Recovered')
				l.append('Dead')
				l.append('Daily Tested')
				l.append('Daily Tested Positive')
				l.append('Daily Tested Negative')
				l.append('Cumulative Tested Positive')
				l.append('Quarantined')
				l.append('Infected Facilities')
				l.append('Quarantined Facilities')
				writer.writerow(l)

				# len used to iterate through every day
				for i in range(self.days):
					l = []
					l.append(i)
					l.append(self.susceptible[i])
					l.append(self.infected[i])
					l.append(self.cumulative_infected[i])
					l.append(self.cumulative_infected_residents[i])
					l.append(self.cumulative_infected_staff[i])
					l.append(self.daily_infected[i])
					l.append(self.daily_infected_residents[i])
					l.append(self.daily_infected_staff[i])
					l.append(self.incubating[i])
					l.append(self.transmitting[i])
					l.append(self.symptomatic[i])
					l.append(self.asymptomatic[i])
					l.append(self.recovered[i])
					l.append(self.residents_recovered[i])
					l.append(self.staff_recovered[i])
					l.append(self.dead[i])
					l.append(self.daily_tested[i])
					l.append(self.daily_tested_positive[i])
					l.append(self.daily_tested_negative[i])
					l.append(self.cumulative_tested_positive[i])
					l.append(self.quarantined[i])
					l.append(self.infected_facilities[i])
					l.append(self.quarantined_facilities[i])
					writer.writerow(l)
			g.close()
		else:
			for f in range(len(self.matric)):
				with open(self.parameters['Output Directory'] + 'facility_' + str(f) + '/' + export_file, 'w', newline = '') as g:
					writer = csv.writer(g)
					l = []
					writer.writerow(l)

					l = []
					l.append('Day')
					l.append('Susceptible')
					l.append('Infected')
					l.append('Cumulative Infected')
					l.append('Cumulative Infected Residents')
					l.append('Cumulative Infected Staff')
					l.append('Daily Infected')
					l.append('Daily Infected Residents')
					l.append('Daily Infected Staff')
					l.append('Incubating')
					l.append('Transmitting')
					l.append('Symptomatic')
					l.append('Asymptomatic')
					l.append('Recovered')
					l.append('Residents Recovered')
					l.append('Staff Recovered')
					l.append('Dead')
					l.append('Daily Tested')
					l.append('Daily Tested Positive')
					l.append('Daily Tested Negative')
					l.append('Cumulative Tested Positive')
					l.append('Quarantined')
					l.append('Infected Facilities')
					l.append('Quarantined Facilities')
					writer.writerow(l)

					# len used to iterate through every day
					for i in range(self.days):
						l = []
						l.append(i)
						l.append(self.susceptible[f][i])
						l.append(self.infected[f][i])
						l.append(self.cumulative_infected[f][i])
						l.append(self.cumulative_infected_residents[f][i])
						l.append(self.cumulative_infected_staff[f][i])
						l.append(self.daily_infected[f][i])
						l.append(self.daily_infected_residents[f][i])
						l.append(self.daily_infected_staff[f][i])
						l.append(self.incubating[f][i])
						l.append(self.transmitting[f][i])
						l.append(self.symptomatic[f][i])
						l.append(self.asymptomatic[f][i])
						l.append(self.recovered[f][i])
						l.append(self.residents_recovered[f][i])
						l.append(self.staff_recovered[f][i])
						l.append(self.dead[f][i])
						l.append(self.daily_tested[f][i])
						l.append(self.daily_tested_positive[f][i])
						l.append(self.daily_tested_negative[f][i])
						l.append(self.cumulative_tested_positive[f][i])
						l.append(self.quarantined[f][i])
						l.append(self.infected_facilities[f][i])
						l.append(self.quarantined_facilities[f][i])
						writer.writerow(l)
				g.close()
