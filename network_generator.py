import numpy as np
import random
#import sparse
from entities import Facility, Resident, Staff
import copy
import pandas as pd
from math import sin, cos, sqrt, atan2, atan, radians, pi, pow
from sklearn.cluster import KMeans

import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

class GenerateNetwork:
	def __init__(self, parameters):
		self.parameters = parameters
		#self.temp_staff = {'A': [], 'B': []}
		self.FACILITIES = []
		self.facility_temp_dict = {}
		self.facilities_temp_sharing_matrix = []
		self.temp_staff = []
		self.all_temp = []
		self.isolated_facilities = []
		self.infected_facilities = set()
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


	def generate_facility_network_plot(self, coords, title, temp_sharing_matrix):
		lats = coords[:,0]
		longs = coords[:,1]
		m = Basemap(
			projection='merc',
			llcrnrlon=-93.857091,
			llcrnrlat=44.688472,
			urcrnrlon=-92.776311,
			urcrnrlat=45.265508,
			lat_ts=0,
			resolution='i',
			suppress_ticks=True)

		mx,my = m(longs, lats)
		pos = {}
		for j in range(len(lats)):
			pos[j] = (mx[j], my[j])

		graph = nx.Graph()
		for i in range(len(temp_sharing_matrix)):
			for j in np.nonzero(temp_sharing_matrix[i])[0]:
				graph.add_edge(i,j)

		# draw
		#nx.draw_networkx(self.G, pos, node_size=10, node_color='blue')
		nx.draw_networkx_nodes(G=graph, pos=pos, node_list=graph.nodes(), node_color='r', alpha=0.8, node_size=10)
		nx.draw_networkx_edges(G=graph, pos=pos, edge_color='y', alpha=0.2, arrows=False)

		# Now draw the map
		m.drawcountries()
		m.drawstates()
		m.drawcounties()
		m.bluemarble()
		plt.title(title)
		plt.savefig(title+'.png', format = "png", dpi = 300)

	def get_facility(self, ind):
		for fac in range(len(self.FACILITIES)):
			if self.FACILITIES[fac]['facility_code'] == ind:
				facility = self.FACILITIES[fac]
		return facility

	def generate_distance_based_facility_network(self ,coords):
		distance_matrix = np.zeros((len(coords), len(coords)))
		# d = []
		# smallest = []
		for i in range(len(coords)):
			# small = 1000
			for j in range(len(coords)):
				distance_matrix[i,j] = self.get_distance(coords[i], coords[j])
				# d.append(distance_matrix[i,j])
				# if small > distance_matrix[i][j] and i != j:
				# 	small = distance_matrix[i][j]
			# smallest.append(small)

		# fig1 = plt.figure()
		# plt.hist(smallest,bins=10)
		# fig1.savefig('Histogram of distances from nearest facilities')
		#
		# fig2 = plt.figure()
		# plt.hist(d,bins=50)
		# fig2.savefig('Histogram of all distances')
		#
		# fig3 = plt.figure()
		# min3 = [j for i in range(len(coords)) for j in sorted(distance_matrix[i])[1:4]]
		# plt.hist(min3, bins=20)
		# fig3.savefig('Histogram of distances from nearest 3 facilities')

		temp_sharing_matrix = np.zeros((len(coords), len(coords)), dtype = int)
		total_graph_degree = sum([facility['temp'] for facility in self.FACILITIES])
		if total_graph_degree%2 != 0:
			self.FACILITIES[0]['temp'] -= 1
			total_graph_degree -= 1

		while (np.sum(temp_sharing_matrix) < total_graph_degree):
			locations_left = [i for i in range(len(distance_matrix)) if
							  np.sum(temp_sharing_matrix[i]) < self.FACILITIES[i]['temp']]
			loc_1 = random.choice(locations_left)
			neighbors = [j for j in range(len(distance_matrix)) if j != loc_1 and j in locations_left]
			if len(neighbors) == 0:
				break
			norm = 1 #max([distance_matrix[loc_1][j] for j in neighbors])
			#distance_weights = [(4*atan(pi*2 - 2*distance_matrix[loc_1, j]/norm) + atan(pi*5 - 3*distance_matrix[loc_1, j]/(2*norm)) + 5*pi/2) for j in neighbors]
			distance_weights = [(300*pow(distance_matrix[loc_1, j], -1.5)) for j in neighbors]
			loc_2 = random.choices(neighbors, distance_weights)[0]
			# loc_2 = neighbors[distance_weights.index(max(distance_weights))]
			temp_sharing_matrix[loc_1, loc_2] += 1
			temp_sharing_matrix[loc_2, loc_1] = temp_sharing_matrix[loc_1, loc_2]

		while (np.sum(temp_sharing_matrix) < total_graph_degree):
			locations_left = [i for i in range(len(distance_matrix)) if
							  np.sum(temp_sharing_matrix[i]) < self.FACILITIES[i]['temp']]
			loc_1 = random.choice(locations_left)
			if (np.sum(temp_sharing_matrix[loc_1]) < self.FACILITIES[loc_1]['temp']):
				if (self.FACILITIES[loc_1]['temp'] - np.sum(temp_sharing_matrix[loc_1])) % 2 != 0:
					neighbors = [j for j in range(len(distance_matrix)) if j != loc_1 and j in locations_left]
					norm = 1#max([distance_matrix[loc_1][j] for j in neighbors])
					distance_weights = [(300*pow(distance_matrix[loc_1, j], -1.5)) for j in neighbors]
					loc_2 = random.choices(neighbors, distance_weights)[0]
					temp_sharing_matrix[loc_1, loc_2] += 1
					temp_sharing_matrix[loc_2, loc_1] = temp_sharing_matrix[loc_1, loc_2]
				else:
					neighbors = [j for j in range(len(distance_matrix)) if
								 j != loc_1 and np.sum(temp_sharing_matrix[j]) >= self.FACILITIES[j]['temp']]
					norm = 1#max([distance_matrix[loc_1][j] for j in neighbors])
					distance_weights = [(300*pow(distance_matrix[loc_1, j], -1.5)) for j in neighbors]
					loc_2 = random.choices(neighbors, distance_weights)[0]

					neighbors_2 = [i for i in np.nonzero(temp_sharing_matrix[loc_2])[0] if i != loc_1]
					loc_3 = random.choice(neighbors_2)
					temp_sharing_matrix[loc_2, loc_3] -= 1
					temp_sharing_matrix[loc_3, loc_2] = temp_sharing_matrix[loc_2, loc_3]

					temp_sharing_matrix[loc_1, loc_2] += 1
					temp_sharing_matrix[loc_2, loc_1] = temp_sharing_matrix[loc_1, loc_2]
					temp_sharing_matrix[loc_1, loc_3] += 1
					temp_sharing_matrix[loc_3, loc_1] = temp_sharing_matrix[loc_1, loc_3]


		self.generate_facility_network_plot(coords, 'Distance based facilities network', temp_sharing_matrix)
		return temp_sharing_matrix

	def generate_temporary_workers(self):
		for facility in self.FACILITIES:
			for i in range(sum(self.facilities_temp_sharing_matrix[facility['facility_code']])):
				employment_type = 1  # Permanent = 0, Temporary = 1
				shared_facilities = [facility['facility_code']]
				s = Staff(employment_type, self.parameters, shared_facilities)
				self.temp_staff[facility['facility_code']].append(s)
				self.all_temp.append(s)
				for f in np.nonzero(self.facilities_temp_sharing_matrix[facility['facility_code']])[0]:
					fac = self.get_facility(f)
					s.update_shared_facilities(fac['facility_code'])
					#self.temp_staff[facility['facility_code']][i].update_shared_facilities(fac['facility_code'])


	def generate_facility(self, facility):
		residents, staff = facility['residents'], facility['staff']
		ind = 0
		people = []
		t_staff = facility['temp']
		p_staff = staff - t_staff

		while(ind < residents):
			gender = random.choices([0, 1], [self.parameters['MALE_PERCENTAGE'], 1 - self.parameters['MALE_PERCENTAGE']])[0]    #Male = 0, Female = 1
			r = Resident(gender, self.parameters)
			people.append(r)
			ind += 1
		while(ind < residents + p_staff):
			employment_type = 0				#Permanent = 0, Temporary = 1
			shared_facilities = [facility['facility_code']]
			s = Staff(employment_type, self.parameters, shared_facilities)
			people.append(s)
			ind += 1
		for ts in self.all_temp:
			if facility['facility_code'] in ts.shared_facilities:
				people.append(ts)
			#ind += 1
		return people, residents, p_staff, t_staff

	def load_coords(self, filename):
		df = pd.read_csv(filename)
		lats = list(df.LATITUDE)
		longs = list(df.LONGITUDE)
		coords = np.array([[float(lats[i]), float(longs[i])] for i in range(len(lats))])
		return coords

	def load_facilities(self, coords):
		FACILITIES = [{'residents':int(self.parameters['Facility residents']),
					   'staff':int(self.parameters['Facility staff']),
					   'temp':int(self.parameters['Facility staff']*self.parameters['TEMP_PERCENTAGE']),
					   'facility_code':i,
					   'affiliation':'A',
					   'facility_type':'Public'} for i in range(len(coords))]
		return FACILITIES

	def get_distance(self, coords_i, coords_j):
		# approximate radius of earth in km
		R = 6373.0
		lat1 = radians(abs(coords_i[0]))
		lon1 = radians(abs(coords_i[1]))
		lat2 = radians(abs(coords_j[0]))
		lon2 = radians(abs(coords_j[1]))
		dlon = abs(lon2 - lon1)
		dlat = abs(lat2 - lat1)
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		distance = R * c# * 1000
		return distance

	def create_clusters(self, number_of_clusters, coords):
		kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(coords)
		l_array = np.array([[label] for label in kmeans.labels_])
		clusters = np.append(coords,l_array,axis=1)
		return clusters

	def generate_clusters(self, total_cluster, coords):
		c = self.create_clusters(total_cluster, coords)
		cluster_ids = [int(i) for i in c[:,2]]
		return cluster_ids

	def generate_interactions(self):
		facilities_coordinates = self.load_coords("HENNEPIN+Ramsey_NH_Facilities.csv")
		self.FACILITIES = self.load_facilities(facilities_coordinates)
		self.facilities_temp_sharing_matrix = self.generate_distance_based_facility_network(facilities_coordinates)

		# self.FACILITIES = [{'residents': 10, 'staff': 5, 'temp':2, 'facility_code': 0, 'affiliation': 'A', 'facility_type': 'Public'},
		# 				   {'residents': 10, 'staff': 5, 'temp':2, 'facility_code': 1, 'affiliation': 'A', 'facility_type': 'Public'},
		# 				   {'residents': 10, 'staff': 5, 'temp':2, 'facility_code': 2, 'affiliation': 'A', 'facility_type': 'Public'},
		# 				   {'residents': 10, 'staff': 5, 'temp':2, 'facility_code': 3, 'affiliation': 'A', 'facility_type': 'Public'}]
		#
		# self.facilities_temp_sharing_matrix = np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])

		self.temp_staff = {facility['facility_code']: [] for facility in self.FACILITIES}
		self.generate_temporary_workers()

		self.matric = []
		#self.parameters['Facilities'] = self.FACILITIES
		for facility in self.FACILITIES:
			people, residents, p_staff, t_staff = self.generate_facility(facility)
			f = Facility(self.parameters, people, p_staff, t_staff, facility)
			self.matric.append(f)

		for day in range(7):
			designated_temps = {fac.facility_code: [] for fac in self.matric}
			day_pool = {fac: [temp for temp in self.temp_staff[fac]] for fac in self.temp_staff}
			facility_left = list(range(len(self.matric)))
			while(len(facility_left) != 0):
				f_id = random.choice(facility_left)
				facility_left.remove(f_id)
				f = self.matric[f_id]

				facility_temp_pool = [temp for temp in day_pool[f.facility_code]]
				for i in np.nonzero(self.facilities_temp_sharing_matrix[:, f.facility_code])[0]:
					fac = self.get_facility(i)
					temp_shared = self.facilities_temp_sharing_matrix[fac['facility_code'], f.facility_code]
					if len(day_pool[fac['facility_code']]) > temp_shared:
						facility_temp_pool.extend([temp for temp in random.sample(day_pool[fac['facility_code']],k=temp_shared)])
					else:
						facility_temp_pool.extend([temp for temp in day_pool[fac['facility_code']]])

				while (len(designated_temps[f.facility_code]) != f.n_t_staff):
					temp = random.choice(facility_temp_pool)
					designated_temps[f.facility_code].append(temp)
					facility_temp_pool.remove(temp)
					if temp in day_pool[f.facility_code]:
						day_pool[f.facility_code].remove(temp)
					else:
						for i in np.nonzero(self.facilities_temp_sharing_matrix[:, f.facility_code])[0]:
							fac = self.get_facility(i)
							if temp in day_pool[fac['facility_code']]:
								day_pool[fac['facility_code']].remove(temp)
					if temp.shared_facilities[0] != f.facility_code:
						reverse_temp = random.choice(day_pool[f.facility_code])
						designated_temps[temp.shared_facilities[0]].append(reverse_temp)
						facility_temp_pool.remove(reverse_temp)
						day_pool[f.facility_code].remove(reverse_temp)


			for f in self.matric:
				temp_workers = [f.people.index(temp) for temp in designated_temps[f.facility_code]]
				daily_contacts = np.zeros([f.n_residents + f.n_staff, f.n_residents + f.n_staff])
				todays_staff = list(range(f.n_residents, f.n_residents + f.n_p_staff)) + temp_workers

				staff_available = copy.deepcopy(todays_staff)
				residents_available = list(range(f.n_residents))
				for r in range(f.n_residents):
					# Resident-Staff interactions
					staff_contacts = 0
					while (staff_contacts != self.parameters['CONTACTS_RS']):
						sc = random.choice(staff_available)
						daily_contacts[r, sc] += 1
						daily_contacts[sc, r] += 1
						staff_contacts += 1
						if sum(daily_contacts[sc]) >= self.parameters['CONTACTS_SR']:
							staff_available.remove(sc)

					# Resident-Resident interactions
					# resident_contacts = np.sum(daily_contacts[r][:f.n_residents])
					# while(resident_contacts != self.parameters['CONTACTS_RR']):
					# 	if len(residents_available) == 1 and residents_available[0] == r:
					# 		break
					# 	rc = random.choice(residents_available)
					# 	if sum(daily_contacts[rc][:f.n_residents]) == self.parameters[
					# 		'CONTACTS_RR']:
					# 		residents_available.remove(rc)
					# 		continue
					# 	if rc != r:
					# 		daily_contacts[r,rc] += 1
					# 		daily_contacts[rc,r] += 1
					# 		resident_contacts += 1

				# Resident-Staff interactions
				degree_count = 0
				while(degree_count < f.n_residents * self.parameters['CONTACTS_RR']):
					person_1 = random.choice(residents_available)
					ra = [person for person in residents_available if person != person_1]
					person_2 = random.choice(ra)
					daily_contacts[person_1, person_2] += 1
					daily_contacts[person_2, person_1] += 1
					degree_count += 2


				# Staff-Staff interactions
				staff_available = copy.deepcopy(todays_staff)
				# for s in range(f.n_residents, f.n_residents+p_staff):
				for s in todays_staff:
					staff_contacts = np.sum(daily_contacts[s][f.n_residents:f.n_residents + f.n_staff])
					while (staff_contacts != self.parameters['CONTACTS_SS']):
						if len(staff_available) == 1 and staff_available[0] == s:
							break
						sc = random.choice(staff_available)
						if sum(daily_contacts[sc][f.n_residents:f.n_residents + f.n_staff]) == self.parameters[
							'CONTACTS_SS']:
							staff_available.remove(sc)
							continue
						if sc != s:
							daily_contacts[s, sc] += 1
							daily_contacts[sc, s] += 1
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
		if person_id < self.matric[facility].n_residents:
			for day in range(7):
				for id in range(self.matric[facility].n_residents):
					self.matric[facility].daily_contacts[day][person_id][id] = 0
					self.matric[facility].daily_contacts[day][id][person_id] = 0

		elif person_id < self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			# print("\n")
			# print("Permanent Staff", person_id)
			# print("Facility:", facility)
			# print("Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff)

			replacement_id = self.matric[facility].n_residents + self.matric[facility].n_p_staff
			employment_type = 2				#Permanent_filler = 2, Temporary_filler = 3
			shared_facilities = [facility]
			new_person = Staff(employment_type, self.parameters, shared_facilities)
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
		elif person_id >= self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			#quarantined_id = person_id - (self.matric[facility].n_residents + self.matric[facility].n_p_staff)
			employment_type = 3				#Permanent_filler = 2, Temporary_filler = 3
			shared_facilities = self.matric[facility].people[person_id].shared_facilities
			new_person = Staff(employment_type, self.parameters, shared_facilities)
			for fac in range(len(self.matric)):
				if self.matric[fac].facility_code in self.matric[facility].people[person_id].shared_facilities:
					# print("\n")
					# print("Temp Staff", person_id)
					# print("Facility:", fac)
					# print("Total People", self.matric[fac].n_residents, self.matric[fac].n_p_staff, self.matric[fac].n_t_staff)
					# print("Shape of facility:", self.matric[fac].daily_contacts[0].shape)

					replacement_id = self.matric[fac].n_residents + self.matric[fac].n_staff
					quarantined_id = np.where(np.array(self.matric[fac].people) == self.matric[facility].people[person_id])[0][0]

					self.matric[fac].people = np.insert(self.matric[fac].people, replacement_id, new_person)
					self.matric[fac].n_t_staff += 1
					self.matric[fac].n_staff += 1
					for day in range(7):
						# print("Before")
						# print("Person_ID sum", person_id, self.matric[fac].daily_contacts[day][:,person_id].sum(0))
						self.add_new_person(day, fac, replacement_id, quarantined_id)
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
			#quarantined_id = person_id - (self.matric[facility].n_residents + self.matric[facility].n_p_staff)
			for fac in range(len(self.matric)):
				if self.matric[fac].facility_code in self.matric[facility].people[person_id].shared_facilities:
					for staff in range(self.matric[fac].n_residents + self.matric[fac].n_p_staff, self.matric[fac].n_residents + self.matric[fac].n_staff):
						if self.matric[fac].people[staff].employment_type == 3:
							replacement_id = staff
							break
					quarantined_id = np.where(self.matric[fac].people == self.matric[facility].people[person_id])[0][0]
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
						self.remove_person(day, fac, replacement_id, quarantined_id)
						# print("After")
						# print("Person_ID sum", person_id, self.matric[fac].daily_contacts[day][:,person_id].sum(0))
						# print("Replacement_ID sum", replacement_id, self.matric[fac].daily_contacts[day][:,replacement_id].sum(0))

					self.matric[fac].people = np.delete(self.matric[fac].people, replacement_id)
					self.matric[fac].n_t_staff -= 1
					self.matric[fac].n_staff -= 1

	def social_distancing(self, facility):
		for day in range(7):
			for i in range(self.matric[facility].n_residents):
				for j in range(self.matric[facility].n_residents):
					self.matric[facility].daily_contacts[day][i,j] = 0
			degree_count = 0
			residents_available = [r for r in range(self.matric[facility].n_residents) if self.matric[facility].people[r].quarantine_status != 1]
			residents_available_count = len(residents_available)
			while (degree_count < residents_available_count * self.parameters['CONTACTS_RR_reduced']):
				person_1 = random.choice(residents_available)
				ra = [person for person in residents_available if person != person_1]
				person_2 = random.choice(ra)
				self.matric[facility].daily_contacts[day][person_1, person_2] += 1
				self.matric[facility].daily_contacts[day][person_2, person_1] += 1
				degree_count += 2

	def isolate_facility(self, day, facility):
		quarantine_day = day%7
		self.isolated_facilities.append(facility)
		#remaining_facilities = [fac for fac in range(len(self.matric)) if fac not in self.isolated_facilities and self.matric[fac].affiliation == self.matric[facility].affiliation]
		# facility_ids = np.nonzero(self.facilities_temp_sharing_matrix[self.matric[facility].facility_code])[0]
		# remaining_facilities = [fac for fac in range(len(self.matric)) if self.matric[fac].facility_code in facility_ids]
		# print('shared facility:', remaining_facilities)
		## Finds temp staff who are working in the current facility on the day of the quarantine
		## Finds the remaining staff who can work and are not quarantined
		isolated_temp_staff = []#np.zeros(self.matric[facility].n_t_staff)
		ist = []
		# remaining_temp_staff = []#np.zeros(self.matric[facility].n_t_staff)
		for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
			if ((self.matric[facility].people[staff].shared_facilities[0] == facility) and (self.matric[facility].people[staff].quarantine_status != 1)):
				isolated_temp_staff.append(self.matric[facility].people[staff])
				ist.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))
			# elif self.matric[facility].daily_contacts[quarantine_day%7][staff].quarantine_days == 0:
			# 	remaining_temp_staff.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))

		# print("Isolated Temp Staff:", isolated_temp_staff)
		## Main Facility ##
		for day_ in range(7):
			# print('DAY:', day_)
			# Find the workers who are working on current day
			working_temp_pool = []
			wp = []
			for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
				if (self.matric[facility].is_working(day_%7, staff)) and (self.matric[facility].people[staff] not in isolated_temp_staff):
					working_temp_pool.append(self.matric[facility].people[staff])
					wp.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))
			random.shuffle(working_temp_pool)

			# print("\n")
			# print("BEFORE")
			# print("**** MAIN FACILITY *****")
			# print("Facility:", facility)
			# print("Total People", self.matric[facility].n_residents, self.matric[facility].n_p_staff, self.matric[facility].n_t_staff, self.matric[facility].n_staff)
			# print("Shape of facility:", self.matric[facility].daily_contacts[day_].shape)
			# print("Isolated Temp Staff:", ist)
			# print("Working Temp Pool:", wp, len(working_temp_pool))
			# print("Before")
			# print("SUM:", np.nonzero(self.matric[facility].daily_contacts[day_][:,list(range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff))].sum(0))[0])

			# for fac in remaining_facilities:
			# 	print("\n")
			# 	print("##### OTHER FACILITY #####")
			# 	print("Facility:", fac)
			# 	print("Total People", self.matric[fac].n_residents, self.matric[fac].n_p_staff, self.matric[fac].n_t_staff, self.matric[fac].n_staff)
			# 	print("Shape of facility:", self.matric[fac].daily_contacts[day_].shape)
			# 	print("SUM:", np.nonzero(self.matric[fac].daily_contacts[day_][:,list(range(self.matric[fac].n_residents+self.matric[fac].n_p_staff, self.matric[fac].n_residents+self.matric[fac].n_staff))].sum(0))[0])

			for available_staff in working_temp_pool:
				working_staff_1 = np.where(np.array(self.matric[facility].people) == available_staff)[0][0]
				fac = available_staff.shared_facilities[0]
				for staff in isolated_temp_staff:
					working_staff_2 = np.where(np.array(self.matric[fac].people) == staff)[0][0]
					if (self.matric[fac].is_working(day_ % 7,working_staff_2)):

						workless_staff_1 = np.where(np.array(self.matric[facility].people) == staff)[0][0]
						self.swap_interactions(day_, facility, working_staff_1, workless_staff_1)

						workless_staff_2 = np.where(np.array(self.matric[fac].people) == available_staff)[0][0]
						self.swap_interactions(day_, fac, working_staff_2, workless_staff_2)
						break

			#
			# for staff in isolated_temp_staff:
			# 	# If the isolated staff is not working today
			# 	if (not self.matric[facility].is_working(day_%7, np.where(np.array(self.matric[facility].people) == staff)[0][0])):
			# 		for fac in remaining_facilities:
			# 			if self.matric[fac].is_working(day_ % 7,np.where(np.array(self.matric[fac].people) == staff)[0][0]):
			# 				print('Isolated staff is workign in facality:', fac)
			#
			# 		print("working temp", working_temp_pool)
			#
			# 		designated_staff = np.where(np.array(self.matric[facility].people) == staff)[0][0]
			# 		available_staff = working_temp_pool[0]
			# 		replacement_staff = np.where(np.array(self.matric[facility].people) == available_staff)[0][0]
			# 		working_temp_pool = working_temp_pool[1:]
			# 		self.swap_interactions(day_, facility, designated_staff, replacement_staff)
			#
			# 		fac = available_staff.shared_facilities[0]
			# 		print('replacing fac', fac)
			# 		designated_staff = np.where(np.array(self.matric[fac].people) == available_staff)[0][0]
			# 		available_staff = np.where(np.array(self.matric[fac].people) == staff)[0][0]
			# 		self.swap_interactions(day_, fac, designated_staff, available_staff)


					# for fac in remaining_facilities:
					# 	if self.matric[fac].is_working(day_ % 7,np.where(np.array(self.matric[fac].people) == staff)[0][0]):
					# 		print('Isolated staff is workign in facality:', fac)

					# designated_staff = np.where(np.array(self.matric[facility].people) == staff)[0][0]
					# available_staff = working_temp_pool[0]
					# replacement_staff = np.where(np.array(self.matric[facility].people) == available_staff)[0][0]
					# working_temp_pool = working_temp_pool[1:]
					# self.swap_interactions(day_, facility, replacement_staff, designated_staff)
					# print("reaches here 000000")
					# Find the facility where it is working and replace the interactions
					# for fac in remaining_facilities:
					# 	if (fac in self.matric[facility].people[replacement_staff].shared_facilities) and (fac in self.matric[facility].people[designated_staff].shared_facilities):
					# 		print("reaches here 1111111", fac)
					# 		if (self.matric[fac].is_working(day_%7, np.where(np.array(self.matric[fac].people) == self.matric[facility].people[designated_staff])[0][0])):# staff + (self.matric[fac].n_residents + self.matric[fac].n_p_staff))):
					# 			print("reaches here 222222222222222222", fac)
					# 			designated_staff = np.where(np.array(self.matric[fac].people) == self.matric[facility].people[designated_staff])[0][0]
					# 			replacement_staff = np.where(np.array(self.matric[fac].people) == self.matric[facility].people[replacement_staff])[0][0]
					# 			self.swap_interactions(day_, fac, replacement_staff, designated_staff)
					# 			break

					# for fac in remaining_facilities:
					# 	if self.matric[fac].is_working(day_ % 7,np.where(np.array(self.matric[fac].people) == staff)[0][0]):
					# 		print('Isolated staff is workign in facality:', fac)
					# 		controlled_staff = np.where(np.array(self.matric[fac].people) == staff)[0][0]
					# 		self.matric[fac].people[controlled_staff] = self.matric[facility].people[replacement_staff]
			#
			#
			# print("\n\nAFTER")
			# print("**** MAIN FACILITY *****")
			# print("SUM:", np.nonzero(self.matric[facility].daily_contacts[day_][:,list(range(self.matric[facility].n_residents+self.matric[facility].n_p_staff, self.matric[facility].n_residents+self.matric[facility].n_staff))].sum(0))[0])
			#
			# for fac in remaining_facilities:
			# 	print("\n")
			# 	print("##### OTHER FACILITY #####")
			# 	print("Facility:", fac)
			# 	print("SUM:", np.nonzero(self.matric[fac].daily_contacts[day_][:,list(range(self.matric[fac].n_residents+self.matric[fac].n_p_staff, self.matric[fac].n_residents+self.matric[fac].n_staff))].sum(0))[0])
			#
			#
