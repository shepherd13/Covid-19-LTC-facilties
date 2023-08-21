import numpy as np
import random
import math
#import sparse
from entities import Facility, Resident, Staff
import copy
import pandas as pd
from math import sin, cos, sqrt, atan2, atan, radians, pi, pow
from sklearn.cluster import KMeans

import networkx as nx
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap as Basemap

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


	# def generate_facility_network_plot(self, coords, title, temp_sharing_matrix):
	# 	lats = coords[:,0]
	# 	longs = coords[:,1]
	# 	m = Basemap(
	# 		projection='merc',
	# 		ellps='WGS84',
	# 		llcrnrlon=-97.33281160702545,
	# 		llcrnrlat=43.2896811867473,
	# 		urcrnrlon=-88.60714488802908,
	# 		urcrnrlat=49.290164788951934,
	# 		lat_ts=0,
	# 		resolution='i',
	# 		suppress_ticks=True)
	# 
	# 	mx,my = m(longs, lats)
	# 	pos = {}
	# 	for j in range(len(lats)):
	# 		pos[j] = (mx[j], my[j])
	# 
	# 	graph = nx.Graph()
	# 	for i in range(len(temp_sharing_matrix)):
	# 		for j in np.nonzero(temp_sharing_matrix[i])[0]:
	# 			graph.add_edge(i,j)
	# 
	# 	# draw
	# 	#nx.draw_networkx(self.G, pos, node_size=10, node_color='blue')
	# 	nx.draw_networkx_nodes(G=graph, pos=pos, node_list=graph.nodes(), node_color='r', alpha=0.8, node_size=10)
	# 	nx.draw_networkx_edges(G=graph, pos=pos, edge_color='y', alpha=0.2, arrows=False)
	# 
	# 	# Now draw the map
	# 	#m.fillcontinents(color='#e6b800', lake_color='#A6CAE0')
	# 	m.drawcountries()
	# 	m.drawstates()
	# 	m.drawcounties()
	# 	m.bluemarble()
	# 	plt.title(title)
	# 	plt.savefig(title+'.png', format = "png", dpi = 300)

	def get_facility(self, ind):
		for fac in range(len(self.FACILITIES)):
			if self.FACILITIES[fac]['facility_code'] == ind:
				facility = self.FACILITIES[fac]
		return facility

	def generate_distance_based_facility_network(self, coords,facility_info):
		df = pd.read_csv('Minnesota_nursing_homes_without external connections.csv')
		facilities = [row['Nursing Home'] for index, row in facility_info.iterrows()]
		temp_sharing_matrix = np.zeros((len(facilities), len(facilities)), dtype = int)
		temp_sharing_matrix_2 = np.zeros((len(facilities), len(facilities)), dtype=int)

		# facility_info[facility_info['Nursing Home']=='lifecare roseau manor'].index.values[0]

		for index, row in df.iterrows():
			temp_sharing_matrix[facilities.index(row['Nursing Home Name'].strip().lower()),
				facilities.index(row['Connected_to'].strip().lower())] = int(row['Strength'])


		for i in range(len(facilities)):
			for j in range(i,len(facilities)):
				temp_sharing_matrix_2[i][j] = temp_sharing_matrix[i][j]
		np.save("temp_rc_network.npy", temp_sharing_matrix)
		return temp_sharing_matrix

	def generate_temporary_workers(self):
		for facility in self.FACILITIES:
			connected_facilities = [i for i in np.nonzero(self.facilities_temp_sharing_matrix[facility['facility_code']])[0] if i > facility['facility_code']]
			for other_facility_code in connected_facilities:
				for i in range(self.facilities_temp_sharing_matrix[facility['facility_code']][other_facility_code]):
					employment_type = 1  # Permanent = 0, Temporary = 1
					shared_facilities = [facility['facility_code'], other_facility_code]
					s = Staff(employment_type, self.parameters, shared_facilities)
					self.temp_staff[facility['facility_code']].append(s)
					self.temp_staff[other_facility_code].append(s)
					self.all_temp.append(s)
		print("ALL TEMPS:", len(self.all_temp))



	def generate_facility(self, facility):
		residents, staff = facility['residents'], facility['staff']
		ind = 0
		people = []
		t_staff = len(self.temp_staff[facility['facility_code']])
		p_staff = staff

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
		return people, residents, p_staff, t_staff

	def load_coords(self, filename):
		df = pd.read_csv(filename)
		lats = list(df.latitude)
		longs = list(df.longitude)
		coords = np.array([[float(lats[i]), float(longs[i])] for i in range(len(lats))])
		return coords

	def load_facilities(self, facility_info):
		FACILITIES = [{'name': row['Nursing Home'],
					   'residents':int(row['Resident Beds']),
					   'staff':math.ceil(int(row['Resident Beds'])/4),
					   'facility_code':index,
					   'affiliation':'A',
					   'facility_type':'Public'} for index, row in facility_info.iterrows()]
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
		distance = R * c
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
		facility_info = pd.read_csv('MN_NursingHomes_beds.csv')
		facilities_coordinates = self.load_coords('MN_NursingHomes_beds.csv')
		self.FACILITIES = self.load_facilities(facility_info)
		self.facilities_temp_sharing_matrix = self.generate_distance_based_facility_network(facilities_coordinates, facility_info)

		self.temp_staff = {facility['facility_code']: [] for facility in self.FACILITIES}
		self.generate_temporary_workers()

		self.matric = []
		total_permanent_staff = 0
		for facility in self.FACILITIES:
			people, residents, p_staff, t_staff = self.generate_facility(facility)
			f = Facility(self.parameters, people, p_staff, t_staff, facility)
			self.matric.append(f)
			total_permanent_staff += p_staff

		print("Permanent staff:", total_permanent_staff)

		for day in range(7):
			print(day)
			designated_temps = {fac.facility_code: [] for fac in self.matric}

			for temp in self.all_temp:
				designated_temps[random.choice(temp.shared_facilities)].append(temp)

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



	def update_interactions_when_person_quarantines(self, facility, person_id):
		# print("################ QUARANTINE STARTS for:", person_id)
		if person_id < self.matric[facility].n_residents:
			for day in range(7):
				for id in range(self.matric[facility].n_residents):
					self.matric[facility].daily_contacts[day][person_id][id] = 0
					self.matric[facility].daily_contacts[day][id][person_id] = 0

		elif person_id < self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			replacement_id = self.matric[facility].n_residents + self.matric[facility].n_p_staff
			employment_type = 2				#Permanent_filler = 2, Temporary_filler = 3
			shared_facilities = [facility]
			new_person = Staff(employment_type, self.parameters, shared_facilities)
			self.matric[facility].people = np.insert(self.matric[facility].people, replacement_id, new_person)
			self.matric[facility].n_p_staff += 1
			self.matric[facility].n_staff += 1
			for day in range(7):
				self.add_new_person(day, facility, replacement_id, person_id)

		elif person_id >= self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			employment_type = 3				#Permanent_filler = 2, Temporary_filler = 3
			shared_facilities = self.matric[facility].people[person_id].shared_facilities
			new_person = Staff(employment_type, self.parameters, shared_facilities)
			for fac in range(len(self.matric)):
				if self.matric[fac].facility_code in self.matric[facility].people[person_id].shared_facilities:
					replacement_id = self.matric[fac].n_residents + self.matric[fac].n_staff
					quarantined_id = np.where(np.array(self.matric[fac].people) == self.matric[facility].people[person_id])[0][0]

					self.matric[fac].people = np.insert(self.matric[fac].people, replacement_id, new_person)
					self.matric[fac].n_t_staff += 1
					self.matric[fac].n_staff += 1
					for day in range(7):
						self.add_new_person(day, fac, replacement_id, quarantined_id)
						

	def update_interactions_when_person_quarantine_ends(self, facility, person_id):
		# Find a replacement filler
		if person_id < self.matric[facility].n_residents + self.matric[facility].n_p_staff:
			for staff in range(self.matric[facility].n_residents, self.matric[facility].n_residents + self.matric[facility].n_p_staff):
				if self.matric[facility].people[staff].employment_type == 2:
					replacement_id = staff
					break

			# Remove the filler
			for day in range(7):
				self.remove_person(day, facility, replacement_id, person_id)

			self.matric[facility].people = np.delete(self.matric[facility].people, replacement_id)
			self.matric[facility].n_p_staff -= 1
			self.matric[facility].n_staff -= 1
		else:
			for fac in range(len(self.matric)):
				if self.matric[fac].facility_code in self.matric[facility].people[person_id].shared_facilities:
					for staff in range(self.matric[fac].n_residents + self.matric[fac].n_p_staff, self.matric[fac].n_residents + self.matric[fac].n_staff):
						if self.matric[fac].people[staff].employment_type == 3:
							replacement_id = staff
							break
					quarantined_id = np.where(self.matric[fac].people == self.matric[facility].people[person_id])[0][0]
					# Remove the filler
					for day in range(7):
						self.remove_person(day, fac, replacement_id, quarantined_id)

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
		isolated_temp_staff = []
		ist = []
		for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
			if ((self.matric[facility].is_working(quarantine_day, staff)) and (self.matric[facility].people[staff].quarantine_status != 1)):
				isolated_temp_staff.append(self.matric[facility].people[staff])
				ist.append(staff - (self.matric[facility].n_residents + self.matric[facility].n_p_staff))

		## Main Facility ##
		for day_ in range(7):
			for staff in range(self.matric[facility].n_residents + self.matric[facility].n_p_staff, self.matric[facility].n_residents + self.matric[facility].n_staff):
				if (self.matric[facility].is_working(day_%7, staff)) and (self.matric[facility].people[staff] not in isolated_temp_staff):
					fac = [f for f in self.matric[facility].people[staff].shared_facilities if f != facility][0]
					working_staff = np.where(np.array(self.matric[fac].people) == self.matric[facility].people[staff])[0][0]
					self.matric[fac].daily_contacts[day_%7][working_staff] = self.matric[fac].daily_contacts[quarantine_day][working_staff]
					self.matric[fac].daily_contacts[day_%7][:,working_staff] = self.matric[fac].daily_contacts[quarantine_day][:,working_staff]
					self.matric[facility].daily_contacts[day_%7][staff] = np.zeros(self.matric[facility].daily_contacts[day_%7].shape[0])
					self.matric[facility].daily_contacts[day_%7][:,staff] = np.zeros(self.matric[facility].daily_contacts[day_%7].shape[1])


