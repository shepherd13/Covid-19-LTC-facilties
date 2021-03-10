class Polilcy:
	def __init__(self, parameters, matric):
		self.parameters = parameters
		self.matric = matric

class ReplacePeople(Polilcy):
	def replace_dead_people(self, day):
		for facility in range(len(self.matric)):
			for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				current_disease_state = self.matric[facility].people[person].get_disease_state(day)
				if current_disease_state == -2 and self.matric[facility].people[person].get_disease_state(day-1) != -2:
					self.matric[facility].update_contacts_when_person_die(person)

		# for person in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
		# 		current_disease_state = self.matric[facility].people[person].get_disease_state(day)
		# 		self.record_states(day, current_disease_state)

