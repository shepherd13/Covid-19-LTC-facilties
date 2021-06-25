import numpy as np
import random
from math import sin, cos, sqrt, atan2, atan, radians, pi

distance_matrix = np.array([[0,1,3,3,3,1],[1,0,2,3,3,1],[3,2,0,2,2,1],[3,3,2,0,4,2],[3,3,2,0,4,1],[1,1,1,2,1,0]])
temp_sharing_matrix = np.zeros((len(distance_matrix),len(distance_matrix)), dtype=int)
total_graph_degree = 30
total_node_degree = 5
count = 0
while(np.sum(temp_sharing_matrix) < total_graph_degree):
	locations_left = [i for i in range(len(distance_matrix)) if np.sum(temp_sharing_matrix[i]) < total_node_degree]
	loc_1 = random.choice(locations_left)
	neighbors = [j for j in range(len(distance_matrix)) if j!=loc_1  and j in locations_left]
	if len(neighbors) == 0:
		break
	distance_weights = [4*(atan(3*pi/2 -distance_matrix[loc_1,j]/2)+pi/2) for j in neighbors]
	loc_2 = random.choices(neighbors, distance_weights)[0]
	temp_sharing_matrix[loc_1, loc_2] += 1
	temp_sharing_matrix[loc_2, loc_1] = temp_sharing_matrix[loc_1, loc_2]

while(np.sum(temp_sharing_matrix) < total_graph_degree):
	locations_left = [i for i in range(len(distance_matrix)) if np.sum(temp_sharing_matrix[i]) < total_node_degree]
	loc_1 = random.choice(locations_left)
	if(np.sum(temp_sharing_matrix[loc_1]) < total_node_degree):
		if (total_node_degree - np.sum(temp_sharing_matrix[loc_1])) % 2 != 0:
			neighbors = [j for j in range(len(distance_matrix)) if j!=loc_1 and j in locations_left]
			distance_weights = [(atan(pi/2 -distance_matrix[loc_1,j])+pi/2) for j in neighbors]
			loc_2 = random.choices(neighbors, distance_weights)[0]
			temp_sharing_matrix[loc_1, loc_2] += 1
			temp_sharing_matrix[loc_2, loc_1] = temp_sharing_matrix[loc_1, loc_2]
		else:
			neighbors = [j for j in range(len(distance_matrix)) if j!=loc_1 and np.sum(temp_sharing_matrix[j]) >= total_node_degree]
			distance_weights = [4*(atan(3*pi/2 -distance_matrix[loc_1,j]/2)+pi/2) for j in neighbors]
			loc_2 = random.choices(neighbors, distance_weights)[0]
			
			neighbors_2 = [i for i in np.nonzero(temp_sharing_matrix[loc_2])[0] if i != loc_1]
			loc_3 = random.choice(neighbors_2)
			temp_sharing_matrix[loc_2, loc_3] -= 1
			temp_sharing_matrix[loc_3, loc_2] = temp_sharing_matrix[loc_2, loc_3]

			temp_sharing_matrix[loc_1, loc_2] += 1
			temp_sharing_matrix[loc_2, loc_1] = temp_sharing_matrix[loc_1, loc_2]
			temp_sharing_matrix[loc_1, loc_3] += 1
			temp_sharing_matrix[loc_3, loc_1] = temp_sharing_matrix[loc_1, loc_3]

