import numpy as np
import random
import sparse
from entities import Facility, Resident, Staff
import copy

# coords = [[],[],[]]
# data = []

def get_temporary_workers(parameters):
	temp_staff = []
	for fac in parameters['Facilities']:
		for i in range(int(fac[1] * parameters['TEMP_PERCENTAGE'])):
			employment_type = 1				#Permanent = 0, Temporary = 1
			s = Staff(employment_type, parameters)
			temp_staff.append(s)
	return temp_staff


def generate_facility(residents, staff, total_temp_staff, parameters):
	ind = 0
	people = []
	t_staff = int(staff * parameters['TEMP_PERCENTAGE'])
	p_staff = staff - t_staff

	while(ind < residents):
		gender = random.choices([0, 1], [parameters['MALE_PERCENTAGE'], 1 - parameters['MALE_PERCENTAGE']])[0]    #Male = 0, Female = 1
		r = Resident(gender, parameters)
		people.append(r)
		ind += 1
	while(ind < residents + p_staff):
		employment_type = 0				#Permanent = 0, Temporary = 1
		s = Staff(employment_type, parameters)
		people.append(s)
		ind += 1
	#while(ind < residents + p_staff + len(total_temp_staff)):
	for i in range(len(total_temp_staff)):
		people.append(total_temp_staff[i])
		#ind += 1
	return people, residents, p_staff, t_staff

def get_staff_interactions(parameters):
	FACILITIES = [[100, 100, 101, 'A', 'Public'],[100, 100, 102, 'A', 'Public'],[100, 100, 103, 'A', 'Public']]
	parameters['Facilities'] = FACILITIES
	facilities = []
	total_temp_staff = get_temporary_workers(parameters)
	for fac in parameters['Facilities']:
		people, residents, p_staff, t_staff = generate_facility(fac[0], fac[1], total_temp_staff, parameters)
		f = Facility(parameters, people, p_staff, t_staff, *fac)
		facilities.append(f)


	for day in range(7):
		#print(day)
		pool_temps = list(range(f.n_residents + f.n_p_staff, f.n_residents + f.n_staff))
		for f in facilities:
			daily_contacts = np.zeros([f.n_residents + f.n_staff, f.n_residents + f.n_staff])
			temp_workers = []
			for i in range(f.n_t_staff):
				random.shuffle(pool_temps)
				temp_workers.append(pool_temps.pop())
			todays_staff = list(range(f.n_residents, f.n_residents+f.n_p_staff)) + temp_workers
			staff_available = copy.deepcopy(todays_staff)
			for r in range(f.n_residents):
				staff_contacts = 0
				while(staff_contacts != parameters['CONTACTS_RS']):
					sc = random.choice(staff_available)
					daily_contacts[r,sc] += 1
					daily_contacts[sc,r] += 1
					staff_contacts += 1
					if sum(daily_contacts[sc]) >= parameters['CONTACTS_RS']:
						staff_available.remove(sc)

				# resident_contacts = 0
				# while(resident_contacts != CONTACTS_RR):
				# 	rc = random.randint(0, RESIDENTS-1)
				# 	if rc != r:
				# 		daily_contacts[r,rc] += 1
				# 		daily_contacts[rc,r] += 1
				# 		resident_contacts += 1

			staff_available = copy.deepcopy(todays_staff)
			#for s in range(f.n_residents, f.n_residents+p_staff):
			for s in todays_staff:
				staff_contacts = np.sum(daily_contacts[s][f.n_residents:f.n_residents + f.n_staff])
				while(staff_contacts != parameters['CONTACTS_SS']):
					if len(staff_available) == 1 and staff_available[0] == s:
						break
					sc = random.choice(staff_available)
					if sum(daily_contacts[sc][f.n_residents:f.n_residents + f.n_staff]) == parameters['CONTACTS_SS']:
							staff_available.remove(sc)
							continue
					if sc != s:
						daily_contacts[s,sc] += 1
						daily_contacts[sc,s] += 1
						staff_contacts += 1

			f.set_daily_contacts(day, daily_contacts)


			# non_zero_coords = np.nonzero(daily_contacts)
			# coords[0].extend([day]*len(non_zero_coords[0]))
			# coords[1].extend(non_zero_coords[0])
			# coords[2].extend(non_zero_coords[1])


			#data.extend(daily_contacts[non_zero_coords])

	#contact_tensor = sparse.COO(coords, data, shape=(DAYS, RESIDENTS+STAFF, RESIDENTS+STAFF))
	#sparse.save_npz('contact_tensor_test.npz', contact_tensor)
	return facilities

