import numpy as np
import random
#import sparse
from entities import Facility, Resident, Staff
import copy

class GenerateNetwork:
	def __init__(self, parameters):
		self.parameters = parameters
		self.temp_staff = []
		self.available_temp_staff = []
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
		self.available_temp_staff = np.ones(len(self.temp_staff))

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
		FACILITIES = [[100, 100, 101, 'A', 'Public'], [100, 100, 102, 'A', 'Public']]#,[100, 100, 103, 'A', 'Public']]
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
						if sum(daily_contacts[sc]) >= self.parameters['CONTACTS_RS']:
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

	def update_contacts_when_person_die(self, facility, person_id):
		if person_id < self.matric[facility].n_residents:
			replacement_id = self.matric[facility].n_residents
		else:
			print("STAFF DIED")
			replacement_id = self.matric[facility].n_residents + self.matric[facility].n_staff

		for day in range(7):
			temp_matrix = np.insert(self.matric[facility].daily_contacts[day], replacement_id, np.zeros(self.matric[facility].daily_contacts[day].shape[0]), 1)
			temp_matrix = np.insert(temp_matrix, replacement_id, np.zeros(temp_matrix.shape[1]), 0)
			temp_matrix[[person_id, replacement_id]] = temp_matrix[[replacement_id, person_id]]
			temp_matrix[:,[person_id, replacement_id]] = temp_matrix[:,[replacement_id, person_id]]
			self.matric[facility].daily_contacts[day] = temp_matrix
		gender = random.choices([0, 1], [self.parameters['MALE_PERCENTAGE'], 1 - self.parameters['MALE_PERCENTAGE']])[0]    #Male = 0, Female = 1
		new_person = Resident(gender, self.parameters)
		self.matric[facility].people = np.insert(self.matric[facility].people, self.matric[facility].n_residents, new_person)
		self.matric[facility].n_residents += 1


	def isolate_facility(self, facility):
		self.isolated_facilities.append(facility)

		temp_workers = []
		for i in range(self.matric[facility].n_t_staff):
			ind = random.choice(self.available_temp_staff.nonzero()[0])
			self.available_temp_staff[ind] = 0
			temp_workers.append(self.matric[facility].n_residents+self.matric[facility].n_p_staff+ind)

		if len(self.available_temp_staff.nonzero()[0]) == 0:
			return

		# print("***********Main Facilities*************")
		for day in range(7):
			# print("day:", day)
			# print("Temp workers:", temp_workers)
			for staff in temp_workers:
				if self.matric[facility].daily_contacts[day][:,staff].sum(0) == 0:
					pool_temps = [s + self.matric[facility].n_residents+self.matric[facility].n_p_staff for s in self.available_temp_staff.nonzero()[0]]
					# print("Available temp_staff:", self.available_temp_staff.nonzero()[0])
					# print("Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff)
					# print("Shape of facility:", self.matric[facility].daily_contacts[day].shape)
					# print("facility:", facility, pool_temps)
					# print("SUM:", self.matric[facility].daily_contacts[day][:,list(range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff))].sum(0))
					
					available_staff = pool_temps[random.choice(self.matric[facility].daily_contacts[day][:,pool_temps].sum(0).nonzero()[0])]
					
					# print("A/S", available_staff, staff)
					# print()
					self.matric[facility].daily_contacts[day][[available_staff, staff]] = self.matric[facility].daily_contacts[day][[staff, available_staff]]
					self.matric[facility].daily_contacts[day][:,[available_staff, staff]] = self.matric[facility].daily_contacts[day][:,[staff, available_staff]]
			# print("SUM:", self.matric[facility].daily_contacts[day][:,list(range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff))].sum(0))
			# print()
			
		# print("***********Other Facilities*************")
		facilitites_left = [fac for fac in range(len(self.matric)) if fac not in self.isolated_facilities]
		for day in range(7):
			# print("day:", day)
			pool_temps = copy.deepcopy(self.available_temp_staff)
			# print("Pool:", pool_temps)
			for fac in facilitites_left:
				for staff in pool_temps.nonzero()[0]:
					if self.matric[fac].daily_contacts[day][:,self.matric[fac].n_residents+self.matric[fac].n_p_staff+staff].sum(0) != 0:
						# print("Fac/staff:", fac, staff)
						pool_temps[staff] = 0
				# print("SUM:", self.matric[fac].daily_contacts[day][:,list(range(self.matric[fac].n_residents+self.matric[fac].n_p_staff, self.matric[fac].n_residents+self.matric[fac].n_staff))].sum(0))
			# print("Pool:", pool_temps)
			# print()

			for fac in facilitites_left:
				temp_workers = []
				available_contacts = []
				for staff in range(len(pool_temps)):
					if self.matric[fac].daily_contacts[day][:,self.matric[fac].n_residents+self.matric[fac].n_p_staff+staff].sum(0) != 0:
						if staff in self.available_temp_staff.nonzero()[0]:
							temp_workers.append(self.matric[fac].n_residents+self.matric[fac].n_p_staff+staff)
						else:
							available_contacts.append(self.matric[fac].n_residents+self.matric[fac].n_p_staff+staff)

				for i in range(len(available_contacts)):
					available_pool_staff = random.choice(pool_temps.nonzero()[0])
					available_contact_staff = random.choice(available_contacts)
					available_contacts.remove(available_contact_staff)
					pool_temps[available_pool_staff] = 0
					available_pool_staff += self.matric[fac].n_residents+self.matric[fac].n_p_staff
					self.matric[fac].daily_contacts[day][[available_pool_staff, available_contact_staff]] = self.matric[fac].daily_contacts[day][[available_contact_staff, available_pool_staff]]
					self.matric[fac].daily_contacts[day][:,[available_pool_staff, available_contact_staff]] = self.matric[fac].daily_contacts[day][:,[available_contact_staff, available_pool_staff]]
				# print("Fac:", fac)
				# print("SUM:", self.matric[fac].daily_contacts[day][:,list(range(self.matric[fac].n_residents+self.matric[fac].n_p_staff, self.matric[fac].n_residents+self.matric[fac].n_staff))].sum(0))
				# print()