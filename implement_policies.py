class Policies:
	def __init__(self, parameters, matric, network):
		self.parameters = parameters
		self.matric = matric
		self.network = network

	def implement_policies(self,day):
		self.replace_dead_people(day)
		self.quarantine_facility(day)

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
				for person in range(self.matric[facility].n_residents+self.matric[facility].n_staff):
					if self.matric[facility].people[person].get_disease_state(day) in [2,3,4]:
						total_infected += 1

				if total_infected/(self.matric[facility].n_residents+self.matric[facility].n_staff) > self.parameters['Quarantine Location Infecion Rate']:
					# print("############### Total Infected:", total_infected, facility)
					self.network.isolate_facility(facility)

