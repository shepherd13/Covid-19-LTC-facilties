# copyright Himanshu Kharkwal, Commercial rights reserved.

# -*- coding: utf-8 -*-
import os
import numpy as np
from pathlib import Path
from multiprocessing import Pool
import time
import copy

from network_generator import GenerateNetwork
from infection_transfer import ProbabilityPerInteraction, InitialInfection, OutsideTransmission
from disease_progression import Covid19_DiseaseProgression
from collect_data import Collect_data
from implement_policies import Policies
from mean_se import get_mean_se

def get_parameters(param_file):
	# Read parameters from file
	base_path = Path(__file__).parent
	params = open(base_path / param_file, 'r')
	parameters = {}  # empty parameter dictionary
	for x in params:
		x = x.rstrip()
		x = x.split(': ')
		try:
			float(x[1])
			parameters[x[0]] = float(x[1])  # creates dictionary with parameters
		except ValueError:
			parameters[x[0]] = x[1]  # creates dictionary with parameters
	params.close()
	return parameters

def get_output_directory(parameters):
	base_path = Path(__file__).parent
	output = base_path / parameters['Output Directory']
	# remove dirctory if empty
	try:
		os.rmdir(output)
	except OSError as ex:
		pass
	os.mkdir(output)
	parameters['Output Directory'] = str(output) + '/'

def run_sim(run, parameters, network):
	days = int(parameters['Days'])
	interactions = network.matric
	# Infection Transfer Models
	ii = InitialInfection(parameters, interactions)
	ppi = ProbabilityPerInteraction(parameters, interactions)
	ot = OutsideTransmission(parameters, interactions)

	# Disease Progression Model
	dp = Covid19_DiseaseProgression(parameters, interactions)

	# Data Collection
	cd = Collect_data(days, interactions)

	# Policy implementation
	rp = Policies(parameters, interactions, network)

	daily_infected = ii.transfer(0)
	for day in range(days):
		daily_infected += ppi.transfer(day)
		#daily_infected += ot.transfer(day)
		dp.disease_progression(day)
		cd.update_states(day, daily_infected)
		rp.implement_policies(day)
		daily_infected = []

	export_file = parameters['Output Directory'] + str(run) + '.csv'
	cd.update_csv(export_file)


def main(param_file):
	parameters = get_parameters(param_file)
	output = get_output_directory(parameters)

	# Interaction Patterns generator
	gn = GenerateNetwork(parameters)
	
	# for day in range(1):
	# 	gn.get_graph_properties(day)


	p = Pool(processes=10)

	for run in range(int(parameters['Runs'])):
		#interactions = ng.get_staff_interactions(parameters)
		network = copy.deepcopy(gn)
		# print("ISOLATED FACILITIES:", network.isolated_facilities)
		# print("############################################################## Run:", run)
		# print("Before:",network.matric[0].n_residents,network.matric[1].n_residents,network.matric[2].n_residents)
		# run_sim(run, parameters, network)
		# print("After:",network.matric[0].n_residents,network.matric[1].n_residents,network.matric[2].n_residents)
		# print("ISOLATED FACILITIES:", network.isolated_facilities)
		p.apply_async(run_sim, args=(run, parameters, network, ))
		# del network
	p.close()
	p.join()
	get_mean_se(parameters)
	return gn

if __name__ == "__main__":
#def run():
	np.seterr(all='raise')
	start_time = time.time()

	cp = main('parameters.txt')

	print("Run Time (seconds): " + str(time.time() - start_time))
	print('Sims Done')