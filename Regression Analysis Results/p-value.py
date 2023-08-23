 # -*- coding: utf-8 -*-
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import ast

import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
from sklearn.metrics import r2_score


##############################################################################################
#                                       LTC Plots(comparision real)
##############################################################################################

def get_parameters(param_file):
    # Read parameters from file
    base_path = Path(__file__).parent
    params = open(base_path / param_file, 'r')
    parameters = {}  # empty parameter dictionary
    for x in params:
        x = x.rstrip()
        x = x.split(': ')
        try:
            parameters[x[0]] = ast.literal_eval(x[1])
        except:
            parameters[x[0]] = x[1]

    params.close()
    return parameters


def get_val(val):
    if parameters['transformation'] == 'arcsinh':
        return np.arcsinh(val)
    else:
        return val

parameters = get_parameters('parameters_regression.txt')

lengths = parameters['lengths']

false_negative_rates = parameters['false_negative_rates']
herd_immunity = parameters['herd_immunity']
temporary_staff = parameters['temporary_staff']


for fnr in false_negative_rates:
    for hi in herd_immunity:
        for ts in temporary_staff:
            folder = parameters['input_file']+"_vac_R"+hi+"_S"+hi+"/"
            for prevalence in ['low', 'high']:
                if prevalence == 'high':
                   prev_rates = parameters['prev_rates_high']
                   pr = parameters['pr_high']
                    
                else:
                    prev_rates = parameters['prev_rates_low']
                    pr = parameters['pr_low']
                
                for l in lengths:
                    policy = "M+SD+TQ_A/"
                    policy_string_1= "Masking,\nSocial Distancing"
                    
                    files = list(range(parameters['simulations'][0]))
                    y1 = []
                    for d in prev_rates:
                        for f in files:
                            df = pd.read_csv(d+policy+folder+str(f)+".csv")
                            val = float(df.loc[df["Day"] == l]["Cumulative Infected"])
                            y1.append(get_val(val))
                            del df

                    policy = "M+SD+TQ_A+IF/"
                    policy_string_2= "Masking,\nSocial Distancing,\nIsolating Facilities"
                    y2 = []
                    for d in prev_rates:
                        for f in files:
                            df = pd.read_csv(d+policy+folder+str(f)+".csv")
                            val = float(df.loc[df["Day"] == l]["Cumulative Infected"])
                            y2.append(get_val(val))
                            del df


                    policy = "BM+SD+TQ_A/"
                    policy_string_3= "Blanket Masking,\nSocial Distancing"
                    y3 = []
                    for d in prev_rates:
                        for f in files:
                            df = pd.read_csv(d+policy+folder+str(f)+".csv")
                            val = float(df.loc[df["Day"] == l]["Cumulative Infected"])
                            y3.append(get_val(val))
                            del df
                    
                    policy = "BM+SD+TQ_A+IF/"
                    policy_string_4 = "Blanket Masking,\nSocial Distancing,\nIsolating Facilities"
                    y4 = []
                    for d in prev_rates:
                        for f in files:
                            df = pd.read_csv(d+policy+folder+str(f)+".csv")
                            val = float(df.loc[df["Day"] == l]["Cumulative Infected"])
                            y4.append(get_val(val))
                    
                    policy = "TQ_A+IF/"
                    policy_string_5 = "Isolating Facilities"
                    y5 = []
                    for d in prev_rates:
                        for f in files:
                            df = pd.read_csv(d+policy+folder+str(f)+".csv")
                            val = float(df.loc[df["Day"] == l]["Cumulative Infected"])
                            y5.append(get_val(val))
                            del df

                    policy = "TQ/"
                    policy_string_6 = "No Policy"
                    y6 = []
                    for d in prev_rates:
                        for f in files:
                            df = pd.read_csv(d+policy+folder+str(f)+".csv")
                            val = float(df.loc[df["Day"] == l]["Cumulative Infected"])
                            y6.append(get_val(val))
                            del df


                    
                    x = [i for i in pr for j in range(parameters['simulations'][0])]

                X_data = np.zeros((6*len(y1),6))
                y_target = np.zeros((6*len(y1)))

                #M+SD
                X_data[:len(y1),0] = x
                X_data[:len(y1),5] = x
                y_target[:len(y1)] = y1

                X_data[len(y1):2*len(y1),0] = x

                #M+SD+IF
                X_data[len(y1):2*len(y1),1] = x
                X_data[len(y1):2*len(y1),5] = x
                y_target[len(y1):2*len(y1)] = y2

                #BM+SD
                X_data[2*len(y1):3*len(y1),2] = x
                X_data[2*len(y1):3*len(y1),5] = x
                y_target[2*len(y1):3*len(y1)] = y3

                X_data[3*len(y1):4*len(y1),2] = x

                #BM+SD+IF
                X_data[3*len(y1):4*len(y1),3] = x
                X_data[3*len(y1):4*len(y1),5] = x
                y_target[3*len(y1):4*len(y1)] = y4


                #(1-M+SD)(1-BM+SD)IF
                X_data[4*len(y1):5*len(y1),4] = x
                X_data[4*len(y1):5*len(y1),5] = x
                y_target[4*len(y1):5*len(y1)] = y5

                #X_data[len(y1):2*len(y1),4] = x
                #X_data[3*len(y1):4*len(y1),4] = x


                #No Policy
                X_data[5*len(y1):6*len(y1),5] = x
                y_target[5*len(y1):6*len(y1)] = y6

                
                ## Outputs ##

                ############################# Save input matrices ##############################
                np.savetxt("main_policy_X-data_prevalence_"+prevalence+"_herdImmunity_"+hi+".csv", X_data, delimiter=",")
                np.savetxt("main_policy_y-data_prevalence_"+prevalence+"_herdImmunity_"+hi+".csv", y_target, delimiter=",")
                ################################################################################

                f = open(parameters['output_file']+"_"+prevalence+"_"+hi+".txt",'w')

                ########################## Naive regression results ###########################
                #X2 = sm.add_constant(X_data[:,4:])
                #est = sm.OLS(y_target, X2)
                #est2 = est.fit()
                #f.write(str(est2.summary(xname=['const', 'IF', 'No Policy'])))
                #f.write('\n\n')
                ##############################################################################

                ############# Without IF, regression results for all policies ################
                #X1 = np.zeros((6*len(y1),5))
                #X1[:,:4] = X_data[:,:4]
                #X1[:,4] = X_data[:,5]
                #X2 = sm.add_constant(X1)
                #est = sm.OLS(y_target, X2)
                #est2 = est.fit()
                #f.write(str(est2.summary(xname=['const','M+SD','M+SD+IF','BM+SD','BM+SD+IF','No Policy'])))
                ##############################################################################

                ####### IF without other controls, regression results for all policies #######
                X2 = sm.add_constant(X_data)
                est = sm.OLS(y_target, X2)
                est2 = est.fit()
                f.write(str(est2.summary(xname=['const','M+SD','M+SD+IF','BM+SD','BM+SD+IF','(1-M+SD)(1-BM+SD)IF','No Policy'])))
                ##############################################################################

                f.close()

