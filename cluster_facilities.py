import pandas as pd
import numpy as np
from math import sin, cos, sqrt, atan2, radians
from geopy.geocoders import Nominatim
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def get_distance(coords_i, coords_j):
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


# locator = Nominatim(user_agent='myGeocoder')
# df = pd.read_csv("MN_NH_Facilities.csv")
# df = df[df['COUNTY_NAME'] == 'HENNEPIN' or df['COUNTY_NAME'] == 'RAMSEY']
# for i in range(df.shape[0]):
# 	try:
# 		location = locator.geocode(df.iloc[i]['ADDRESS'] + ', ' + df.iloc[i]['CITY'] + ', Minnesota')
# 		df.loc[i, 'LATITUDE'] = str(location.latitude)
# 		df.loc[i, 'LONGITUDE'] = str(location.longitude)
# 	except:
# 		pass

df = pd.read_csv("HENNEPIN+Ramsey_NH_Facilities.csv")


lats = list(df.LATITUDE)
longs = list(df.LONGITUDE)
coords = np.array([[float(lats[i]), float(longs[i])] for i in range(len(lats))])

FACILITIES = [[200, 100, 101, 'A', 'Public'], [100, 50, 102, 'A', 'Public'], [20, 10, 103, 'A', 'Public']]
self.facility_temp_matrix = {101:[(102,0.8),(103,0.2)],102:[(101,1.0)],103:[(101,1.0)]}

def create_facility_network():
    nearby_locs = {}
    for i in range(len(coords)):
        count_5 = 0
        count_10 = 0
        for j in range(len(coords)):
            if (i != j):
                dist = get_distance(coords[i], coords[j])
                if (5 > dist):
                    count_5 += 1
                else:
                    count_10 += 1

        nearby_locs[i] = [(5, count_5), (10, count_10)]


    self.FACILITIES = []

    ts_distribution = {1:[1.0], 2:[0.6,0.4], 3:[0.4,0.4,0.2]}
    self.facility_temp_matrix = {}
    for i in range(len(coords)):
        self.FACILITIES.append([int(self.parameters['Facility residents']), int(self.parameters['Facility staff']), i, 'A', 'Public'])
        self.facility_temp_matrix[i] = []
        c = 0
        if nearby_locs[i][0][1] > 0 and nearby_locs[i][0][1] <= 3:
            for j in range(len(coords)):
                if (i != j):
                    if get_distance(coords[i], coords[j]) < 5:
                        self.facility_temp_matrix[i].append((j, ts_distribution[nearby_locs[i][0][1]][c]))
                        c += 1

        elif nearby_locs[i][0][1] > 3:
            distances = []
            c = 0
            for j in range(len(coords)):
                if (i != j):
                    if get_distance(coords[i], coords[j]) < 5:
                        distances.append(j)
                        c += 1
                        if c == 3:
                            break
            distances = random.sample(distances, 3)
            self.facility_temp_matrix[i] = [((distances[k], ts_distribution[3][k])) for k in range(distances)]

        else:
            smallest = 1000
            s = 0
            for j in range(len(coords)):
                if (i!=j):
                    dist = get_distance(coords[i], coords[j])
                    if (smallest > dist):
                        smallest = dist
                        s = j
            self.facility_temp_matrix[i] = [(s, ts_distribution[1][0])]



# s_array = []
# for i in range(len(coords)):
# 	smallest = 1000
# 	for j in range(len(coords)):
# 		if (i!=j):
# 			dist = get_distance(coords[i], coords[j])/1000
# 			if (smallest > dist):
# 				smallest = dist
# 	s_array.append(smallest


# coords = np.array([[33.    , 41.    ],
#        [33.9693, 41.3923],
#        [33.6074, 41.277 ],
#        [34.4823, 41.919 ],
#        [34.3702, 41.1424],
#        [34.3931, 41.078 ],
#        [34.2377, 41.0576],
#        [34.2395, 41.0211],
#        [34.4443, 41.3499],
#        [34.3812, 40.9793]])



def create_clusters(number_of_clusters,coords):
    kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(coords)
    l_array = np.array([[label] for label in kmeans.labels_])
    clusters = np.append(coords,l_array,axis=1)
    return clusters

def validate_solution(max_dist,clusters):
    _, __, n_clust = clusters.max(axis=0)
    n_clust = int(n_clust)
    for i in range(n_clust):
        two_d_cluster=clusters[clusters[:,2] == i][:,np.array([True, True, False])]
        if not validate_cluster(max_dist,two_d_cluster):
            return False
        else:
            continue
    return True

def validate_cluster(max_dist,cluster):
    distances = cdist(cluster,cluster, lambda ori,des: int(round(get_distance(ori,des))))
    print(distances)
    print(30*'-')
    for item in distances.flatten():
        if item > max_dist:
            return False
    return True

# if __name__ == '__main__':
    # for i in [5,10,15,20,25]:
    #     print(i)
    #     print(validate_solution(10,create_clusters(i,coords)))
    # # c = create_clusters(15,coords)
    # # cluster_ids = [int(i) for i in c[:,2]]
    #
    #
    #
    # for i, label in enumerate(cluster_ids):
    #     plt.text(coords[i][0], coords[i][1],label)