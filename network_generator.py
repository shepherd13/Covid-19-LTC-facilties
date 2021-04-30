import numpy as np
import random
#import sparse
from entities import Facility, Resident, Staff
import copy

class GenerateNetwork:
	def __init__(self, parameters):
		self.parameters = parameters
		self.temp_staff = []
		self.isolated_facilities = []
		self.generate_interactions()

	def __del__(self):
		pass

	def get_graph_properties(self, day):
		from numpy import linalg as LA
		import matplotlib.pyplot as plt
		import networkx as nx

		adjacency_matrix = self.matric[0].daily_contacts[day]
		w, v = LA.eig(adjacency_matrix)
		G = nx.from_numpy_matrix(adjacency_matrix, parallel_edges=True)
		print("Graph Statistics")
		print("Average clustering:", nx.average_clustering(G))
		print("Diameter:", nx.diameter(G))
		# print("Eigenvector Centrality", nx.eigenvector_centrality(G))
		# print("\n")
		print("Average Degree:", G.order()/G.size())
		print("Eigenvalues:", sorted(w)[-2:])

		degrees = [degree_tuple[1] for degree_tuple in nx.degree(G)] # dictionary node:degree
		values = sorted(set(degrees))
		hist = [degrees.count(x) for x in values]

		plt.figure() # you need to first do 'import pylabas plt'
		plt.grid(True)
		plt.plot(values, hist, 'ro-') # in-degree
		#plt.plot(out_values, out_hist, 'bv-') # out-degree
		#plt.legend(['In-degree', 'Out-degree'])
		plt.xlabel('Degree')
		plt.ylabel('Number of nodes')
		plt.title('Degree Distribution of Network of residents and staff in a facility')
		#plt.xlim([0, 2*10**2])
		plt.savefig('Degree_Distribution_1.png')
		plt.close()

		plt.figure()
		degrees = np.sum(adjacency_matrix, 0)
		num_bins = 10
		n, bins, patches = plt.hist(degrees, num_bins, facecolor='blue', alpha=0.5)
		plt.xticks(np.arange(0, 9, 1))
		plt.xlabel('Degree')
		plt.ylabel('Number of nodes')
		plt.title('Degree Distribution of Network of residents and staff in a facility')
		plt.savefig('Degree_Distribution_2.png')
		plt.close()


	def generate_random_network(self):
		FACILITIES = [[100, 100, 101, 'A', 'Public']]
		self.parameters['Facilities'] = FACILITIES
		self.matric = []
		self.generate_temporary_workers()
		for fac in self.parameters['Facilities']:
			people, residents, p_staff, t_staff = self.generate_facility(fac[0], fac[1])
			f = Facility(self.parameters, people, p_staff, t_staff, *fac)
			self.matric.append(f)


		for day in range(7):
			#print(day)
			#pool_temps = list(range(f.n_residents + f.n_p_staff, f.n_residents + f.n_staff))
			pool_temps = np.ones(len(self.temp_staff))
			for f in self.matric:
				daily_contacts = np.zeros([f.n_residents + f.n_staff, f.n_residents + f.n_staff])
				temp_workers = []
				for i in range(f.n_t_staff):
					ind = random.choice(pool_temps.nonzero()[0])
					pool_temps[ind] = 0
					temp_workers.append(f.n_residents+f.n_p_staff+ind)
				todays_staff = list(range(f.n_residents+f.n_staff))

				staff_available = copy.deepcopy(todays_staff)
				for r in range(f.n_residents):
					staff_contacts = 0
					while(staff_contacts != 6):
						if len(staff_available) == 0:
							break
						sc = random.choice(staff_available)
						if sc != r:
							daily_contacts[r,sc] += 1
							daily_contacts[sc,r] += 1
							staff_contacts += 1
							if sum(daily_contacts[sc]) >= 6:
								staff_available.remove(sc)
				f.set_daily_contacts(day, daily_contacts)


	def generate_temporary_workers(self):
		for fac in self.parameters['Facilities']:
			for i in range(int(fac[1] * self.parameters['TEMP_PERCENTAGE'])):
				employment_type = 1				#Permanent = 0, Temporary = 1
				s = Staff(employment_type, self.parameters)
				self.temp_staff.append(s)

	def generate_facility(self, residents, staff):
		ind = 0
		people = []
		t_staff = int(staff * self.parameters['TEMP_PERCENTAGE'])
		p_staff = staff - t_staff

		while(ind < residents):
			gender = random.choices([0, 1], [self.parameters['MALE_PERCENTAGE'], 1 - self.parameters['MALE_PERCENTAGE']])[0]    #Male = 0, Female = 1
			r = Resident(gender, self.parameters)
			people.append(r)
			ind += 1
		while(ind < residents + p_staff):
			employment_type = 0				#Permanent = 0, Temporary = 1
			s = Staff(employment_type, self.parameters)
			people.append(s)
			ind += 1
		#while(ind < residents + p_staff + len(total_temp_staff)):
		for i in range(len(self.temp_staff)):
			people.append(self.temp_staff[i])
			#ind += 1
		return people, residents, p_staff, t_staff


	def generate_interactions(self):
		FACILITIES = [[100, 50, 101, 'A', 'Public'], [100, 50, 102, 'A', 'Public']]#,[100, 100, 103, 'A', 'Public']]
		self.parameters['Facilities'] = FACILITIES
		self.matric = []
		self.generate_temporary_workers()
		for fac in self.parameters['Facilities']:
			people, residents, p_staff, t_staff = self.generate_facility(fac[0], fac[1])
			f = Facility(self.parameters, people, p_staff, t_staff, *fac)
			self.matric.append(f)


		for day in range(7):
			#print(day)
			#pool_temps = list(range(f.n_residents + f.n_p_staff, f.n_residents + f.n_staff))
			pool_temps = np.ones(len(self.temp_staff))
			for f in self.matric:
				daily_contacts = np.zeros([f.n_residents + f.n_staff, f.n_residents + f.n_staff])
				temp_workers = []
				for i in range(f.n_t_staff):
					ind = random.choice(pool_temps.nonzero()[0])
					pool_temps[ind] = 0
					temp_workers.append(f.n_residents+f.n_p_staff+ind)
				todays_staff = list(range(f.n_residents, f.n_residents+f.n_p_staff)) + temp_workers
				# Resident-Staff interactions
				staff_available = copy.deepcopy(todays_staff)
				for r in range(f.n_residents):
					staff_contacts = 0
					while(staff_contacts != self.parameters['CONTACTS_RS']):
						sc = random.choice(staff_available)
						daily_contacts[r,sc] += 1
						daily_contacts[sc,r] += 1
						staff_contacts += 1
						if sum(daily_contacts[sc]) >= self.parameters['CONTACTS_SR']:
							staff_available.remove(sc)

					# resident_contacts = 0
					# while(resident_contacts != CONTACTS_RR):
					# 	rc = random.randint(0, RESIDENTS-1)
					# 	if rc != r:
					# 		daily_contacts[r,rc] += 1
					# 		daily_contacts[rc,r] += 1
					# 		resident_contacts += 1

				# Staff-Staff interactions
				staff_available = copy.deepcopy(todays_staff)
				#for s in range(f.n_residents, f.n_residents+p_staff):
				for s in todays_staff:
					staff_contacts = np.sum(daily_contacts[s][f.n_residents:f.n_residents + f.n_staff])
					while(staff_contacts != self.parameters['CONTACTS_SS']):
						if len(staff_available) == 1 and staff_available[0] == s:
							break
						sc = random.choice(staff_available)
						if sum(daily_contacts[sc][f.n_residents:f.n_residents + f.n_staff]) == self.parameters['CONTACTS_SS']:
								staff_available.remove(sc)
								continue
						if sc != s:
							daily_contacts[s,sc] += 1
							daily_contacts[sc,s] += 1
							staff_contacts += 1

				f.set_daily_contacts(day, daily_contacts)


	def add_new_person(self, day, facility, replacement, designated):
		self.matric[facility].daily_contacts[day] = np.insert(self.matric[facility].daily_contacts[day], replacement, np.zeros(self.matric[facility].daily_contacts[day].shape[0]), 1)
		self.matric[facility].daily_contacts[day] = np.insert(self.matric[facility].daily_contacts[day], replacement, np.zeros(self.matric[facility].daily_contacts[day].shape[1]), 0)
		self.swap_interactions(day, facility, replacement, designated)

	def remove_person(self, day, facility, replacement, designated):
		self.swap_interactions(day, facility, replacement, designated)
		self.matric[facility].daily_contacts[day] = np.delete(self.matric[facility].daily_contacts[day], replacement, 1)
		self.matric[facility].daily_contacts[day] = np.delete(self.matric[facility].daily_contacts[day], replacement, 0)

	def swap_interactions(self, day, facility, replacement, designated):
		self.matric[facility].daily_contacts[day][[replacement, designated]] = self.matric[facility].daily_contacts[day][[designated, replacement]]
		self.matric[facility].daily_contacts[day][:,[replacement, designated]] = self.matric[facility].daily_contacts[day][:,[designated, replacement]]


	def update_interactions_when_person_dies(self, facility, person_id):
		if person_id < self.matric[facility].n_residents:
			replacement_id = self.matric[facility].n_residents
			gender = random.choices([0, 1], [self.parameters['MALE_PERCENTAGE'], 1 - self.parameters['MALE_PERCENTAGE']])[0]    #Male = 0, Female = 1
			new_person = Resident(gender, self.parameters)
			self.matric[facility].people = np.insert(self.matric[facility].people, self.matric[facility].n_residents, new_person)
			self.matric[facility].n_residents += 1

			for day in range(7):
				self.add_new_person(day, facility, replacement_id, person_id)
		else:
			print("MAJOR ERROR::::::::::::::::::::::STAFF DIED")
			#replacement_id = self.matric[facility].n_residents + self.matric[facility].n_staff


	def update_interactions_when_person_quarantines(self, facility, person_id):
		# print("################ QUARANTINE STARTS for:", person_id)
		if person_id < self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			# print("\n")
			# print("Permanent Staff", person_id)
			# print("Facility:", facility)
			# print("Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff)

			replacement_id = self.matric[facility].n_residents + self.matric[facility].n_p_staff
			employment_type = 2				#Permanent_filler = 2, Temporary_filler = 3
			new_person = Staff(employment_type, self.parameters)
			self.matric[facility].people = np.insert(self.matric[facility].people, replacement_id, new_person)
			self.matric[facility].n_p_staff += 1
			self.matric[facility].n_staff += 1
			for day in range(7):
				# print("Before")
				# print("Person_ID sum", person_id, self.matric[facility].daily_contacts[day][:,person_id].sum(0))
				#print("Replacement_ID sum", replacement_id, self.matric[facility].daily_contacts[day][:,replacement_id].sum(0))
				self.add_new_person(day, facility, replacement_id, person_id)
				# print("After")
				# print("Person_ID sum", person_id, self.matric[facility].daily_contacts[day][:,person_id].sum(0))
				# print("Replacement_ID sum", replacement_id, self.matric[facility].daily_contacts[day][:,replacement_id].sum(0))


		else:
			quarantined_id = person_id - (self.matric[facility].n_residents + self.matric[facility].n_p_staff)
			employment_type = 3				#Permanent_filler = 2, Temporary_filler = 3
			new_person = Staff(employment_type, self.parameters)
			for fac in range(len(self.matric)):
				# print("\n")
				# print("Temp Staff", person_id)
				# print("Facility:", fac)
				# print("Total People", self.matric[fac].n_residents, self.matric[fac].n_p_staff, self.matric[fac].n_t_staff)
				# print("Shape of facility:", self.matric[fac].daily_contacts[0].shape)

				replacement_id = self.matric[fac].n_residents + self.matric[fac].n_staff
				person_id = quarantined_id + (self.matric[fac].n_residents + self.matric[fac].n_p_staff)
				
				self.matric[fac].people = np.insert(self.matric[fac].people, replacement_id, new_person)
				self.matric[fac].n_t_staff += 1
				self.matric[fac].n_staff += 1
				for day in range(7):
					# print("Before")
					# print("Person_ID sum", person_id, self.matric[fac].daily_contacts[day][:,person_id].sum(0))
					self.add_new_person(day, fac, replacement_id, person_id)
					# print("After")
					# print("Person_ID sum", person_id, self.matric[fac].daily_contacts[day][:,person_id].sum(0))
					# print("Replacement_ID sum", replacement_id, self.matric[fac].daily_contacts[day][:,replacement_id].sum(0))


	def update_interactions_when_person_quarantine_ends(self, facility, person_id):
		# Find a replacement filler
		# print("################ QUARANTINE ENDS for:", person_id)
		if person_id < self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			for staff in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				if self.matric[facility].people[staff].employment_type == 2:
					replacement_id = staff
					break
			# print("\n")
			# print("Permanent Staff", person_id)
			# print("Facility:", facility)
			# print("Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff)
			# print("Shape of facility:", self.matric[facility].daily_contacts[0].shape)
			# Remove the filler
			for day in range(7):
				# print("Before")
				# print("Person_ID sum", person_id, self.matric[facility].daily_contacts[day][:,person_id].sum(0))
				# print("Replacement_ID sum", replacement_id, self.matric[facility].daily_contacts[day][:,replacement_id].sum(0))
				self.remove_person(day, facility, replacement_id, person_id)
				# print("After")
				# print("Person_ID sum", person_id, self.matric[facility].daily_contacts[day][:,person_id].sum(0))
				#print("Replacement_ID sum", replacement_id, self.matric[facility].daily_contacts[day][:,replacement_id].sum(0))

			self.matric[facility].people = np.delete(self.matric[facility].people, replacement_id)
			self.matric[facility].n_p_staff -= 1
			self.matric[facility].n_staff -= 1
			# print("AFTER Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff)
			# print("AFTER Shape of facility:", self.matric[facility].daily_contacts[0].shape)
		else:
			quarantined_id = person_id - (self.matric[facility].n_residents + self.matric[facility].n_p_staff)
			for fac in range(len(self.matric)):
				for staff in range(self.matric[fac].n_residents + self.matric[fac].n_p_staff, self.matric[fac].n_residents + self.matric[fac].n_staff):
					if self.matric[fac].people[staff].employment_type == 3:
						replacement_id = staff
						break
				person_id = quarantined_id + (self.matric[fac].n_residents + self.matric[fac].n_p_staff)
				# print("\n")
				# print("Temp Staff", person_id)
				# print("Facility:", fac)
				# print("Total People", self.matric[fac].n_residents, self.matric[fac].n_p_staff, self.matric[fac].n_t_staff)
				# print("Shape of facility:", self.matric[fac].daily_contacts[0].shape)
				# Remove the filler
				for day in range(7):
					# print("Before")
					# print("Person_ID sum", person_id, self.matric[fac].daily_contacts[day][:,person_id].sum(0))
					# print("Replacement_ID sum", replacement_id, self.matric[fac].daily_contacts[day][:,replacement_id].sum(0))
					self.remove_person(day, fac, replacement_id, person_id)
					# print("After")
					# print("Person_ID sum", person_id, self.matric[fac].daily_contacts[day][:,person_id].sum(0))
					# print("Replacement_ID sum", replacement_id, self.matric[fac].daily_contacts[day][:,replacement_id].sum(0))

				self.matric[fac].people = np.delete(self.matric[fac].people, replacement_id)
				self.matric[fac].n_t_staff -= 1
				self.matric[fac].n_staff -= 1


	def isolate_facility(self, day, facility):
		quarantine_day = day%7
		self.isolated_facilities.append(facility)
		remaining_facilities = [fac for fac in range(len(self.matric)) if fac not in self.isolated_facilities]

		## Finds temp staff who are working in the current facility on the day of the quarantine
		## Finds the remaining staff who can work and are not quarantined
		isolated_temp_staff = []#np.zeros(self.matric[facility].n_t_staff)
		# remaining_temp_staff = []#np.zeros(self.matric[facility].n_t_staff)
		for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
			if (self.matric[facility].is_working(quarantine_day%7, staff)):
				isolated_temp_staff.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))
			# elif self.matric[facility].daily_contacts[quarantine_day%7][staff].quarantine_days == 0:
			# 	remaining_temp_staff.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))

		# print("Isolated Temp Staff:", isolated_temp_staff)
		## Main Facility ##
		for day in range(7):
			# Find the workers who are working on current day
			working_temp_pool = []
			for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
				if (self.matric[facility].is_working(day%7, staff)) and (staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff) not in isolated_temp_staff):
					working_temp_pool.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))
			random.shuffle(working_temp_pool)

			# print("\n")
			# print("BEFORE")
			# print("**** MAIN FACILITY *****")
			# print("Facility:", facility)
			# print("Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff)
			# print("Shape of facility:", self.matric[facility].daily_contacts[day].shape)
			# print("Working Temp Pool:", working_temp_pool)
			# print("Before")
			# print("SUM:", self.matric[facility].daily_contacts[day][:,list(range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff))].sum(0))

			# for fac in remaining_facilities:
			# 	print("\n")
			# 	print("##### OTHER FACILITY #####")
			# 	print("Facility:", fac)
			# 	print("Total People", self.matric[fac].n_residents, self.matric[fac].n_p_staff, self.matric[fac].n_t_staff)
			# 	print("Shape of facility:", self.matric[fac].daily_contacts[day].shape)
			# 	print("SUM:", self.matric[fac].daily_contacts[day][:,list(range(self.matric[fac].n_residents+self.matric[fac].n_p_staff, self.matric[fac].n_residents+self.matric[fac].n_staff))].sum(0))

			for staff in isolated_temp_staff:
				# If the isolated staff is not working today
				if (not self.matric[facility].is_working(day%7, staff + (self.matric[facility].n_residents + self.matric[facility].n_p_staff))):
					# print("Going insidefor staff:", staff)
					designated_staff = staff + (self.matric[facility].n_residents + self.matric[facility].n_p_staff)
					available_staff = working_temp_pool[0]
					# print("Replacement staff:", available_staff)
					replacement_staff = available_staff + (self.matric[facility].n_residents + self.matric[facility].n_p_staff)
					working_temp_pool = working_temp_pool[1:]
					self.swap_interactions(day, facility, replacement_staff, designated_staff)
					# Find the facility where it is working and replace the interactions
					for fac in remaining_facilities:
						if (self.matric[fac].is_working(day%7, staff + (self.matric[fac].n_residents + self.matric[fac].n_p_staff))):
							designated_staff = staff + (self.matric[fac].n_residents + self.matric[fac].n_p_staff)
							replacement_staff = available_staff + (self.matric[fac].n_residents + self.matric[fac].n_p_staff)
							self.swap_interactions(day, fac, replacement_staff, designated_staff)

			# print("AFTER")
			# print("**** MAIN FACILITY *****")
			# print("SUM:", self.matric[facility].daily_contacts[day][:,list(range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff))].sum(0))

			# for fac in remaining_facilities:
			# 	print("\n")
			# 	print("##### OTHER FACILITY #####")
			# 	print("Facility:", fac)
			# 	print("SUM:", self.matric[fac].daily_contacts[day][:,list(range(self.matric[fac].n_residents+self.matric[fac].n_p_staff, self.matric[fac].n_residents+self.matric[fac].n_staff))].sum(0))
	  
