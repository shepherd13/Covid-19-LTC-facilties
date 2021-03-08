# copyright Himanshu Kharkwal, Commercial rights reserved.

# -*- coding: utf-8 -*-
import os
import numpy as np
from pathlib import Path
from multiprocessing import Pool
import time

import network_generator as ng
from infection_transfer import ProbabilityPerInteraction, InitialInfection
from disease_progression import Covid19_DiseaseProgression
from collect_data import Collect_data
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

def run_sim(run, parameters, interactions):
	days = int(parameters['Days'])
	ii = InitialInfection(parameters, interactions)
	ppi = ProbabilityPerInteraction(parameters, interactions)
	dp = Covid19_DiseaseProgression(parameters, interactions)
	cd = Collect_data(days, interactions)

	daily_infected = ii.transfer(0)
	for day in range(days):
		daily_infected += ppi.transfer(day)
		dp.disease_progression(day)
		cd.update_states(day, daily_infected)
		daily_infected = 0

	export_file = parameters['Output Directory'] + str(run) + '.csv'
	cd.update_csv(export_file)


def main(param_file):
	parameters = get_parameters(param_file)
	output = get_output_directory(parameters)

	#p = Pool(processes=100)  # max 10 processes
	interactions = ng.get_staff_interactions(parameters)

	p = Pool(processes=10)

	for run in range(int(parameters['Runs'])):
		#run_sim(run, parameters, interactions)
		p.apply_async(run_sim, args=(run, parameters, interactions, ))
	p.close()
	p.join()
	get_mean_se(parameters)

if __name__ == "__main__":
	#def run():
	np.seterr(all='raise')
	start_time = time.time()

	main('parameters.txt')

	print("Run Time (seconds): " + str(time.time() - start_time))
	print('Sims Done')