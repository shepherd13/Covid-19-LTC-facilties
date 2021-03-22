import csv
import numpy as np

class Collect_data:
	def __init__(self, days, matric):
		self.days = days
		self.matric = matric
		self.susceptible = [0] * self.days
		self.infected = [0] * self.days
		self.cumulative_infected = [0] * self.days
		self.daily_infected = [0] * self.days
		self.incubating = [0] * self.days
		self.transmitting = [0] * self.days
		self.symptomatic = [0] * self.days
		self.asymptomatic = [0] * self.days
		self.recovered = [0] * self.days
		self.residents_recovered = [0] * self.days
		self.staff_recovered = [0] * self.days
		self.dead = [0] * self.days

	def record_states(self, day, person, facility):
		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		if(current_disease_state == 0):
			self.susceptible[day] += 1

		elif(current_disease_state == 1):
			self.incubating[day] += 1
			self.infected[day] += 1          

		elif(current_disease_state == 2):
			self.transmitting[day] += 1 
			self.infected[day] += 1

		elif(current_disease_state == 3):
			self.transmitting[day] += 1
			self.symptomatic[day] += 1
			self.infected[day] += 1

		elif(current_disease_state == 4):
			self.transmitting[day] += 1
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

	def update_states(self, day, daily_infected):
		for facility in range(len(self.matric)):
			for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				current_disease_state = self.matric[facility].people[person].get_disease_state(day)
				self.record_states(day, person, facility)
				# set states for next day
				if (day + 1) != self.days:
					self.matric[facility].people[person].update_disease_state(day + 1, current_disease_state)


		for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
				current_disease_state = self.matric[facility].people[person].get_disease_state(day)
				self.record_states(day, person, facility)
				# set states for next day
				if (day + 1) != self.days:
					self.matric[facility].people[person].update_disease_state(day + 1, current_disease_state)

		self.daily_infected[day] = np.sum(daily_infected)
		self.cumulative_infected[day] = np.sum(daily_infected)
		if day > 0:
			self.cumulative_infected[day] += self.cumulative_infected[day-1]
			self.recovered[day] += self.recovered[day-1]
			self.residents_recovered[day] += self.residents_recovered[day-1]
			self.staff_recovered[day] += self.staff_recovered[day-1]


	def update_csv(self, export_file):
		with open(export_file, 'w', newline = '') as f:
			writer = csv.writer(f)
			l = []
			writer.writerow(l)

			l = []
			l.append('Day')
			l.append('Susceptible')
			l.append('Infected')
			l.append('Cumulative Infected')
			l.append('Daily Infected')
			l.append('Incubating')
			l.append('Transmitting')
			l.append('Symptomatic')
			l.append('Asymptomatic')
			l.append('Recovered')
			l.append('Residents Recovered')
			l.append('Staff Recovered')
			l.append('Dead')
			writer.writerow(l)

			# len used to iterate through every day
			for i in range(self.days):
				l = []
				l.append(i)
				l.append(self.susceptible[i])
				l.append(self.infected[i])
				l.append(self.cumulative_infected[i])
				l.append(self.daily_infected[i])
				l.append(self.incubating[i])
				l.append(self.transmitting[i])
				l.append(self.symptomatic[i])
				l.append(self.asymptomatic[i])
				l.append(self.recovered[i])
				l.append(self.residents_recovered[i])
				l.append(self.staff_recovered[i])
				l.append(self.dead[i])
				writer.writerow(l)
		f.close()