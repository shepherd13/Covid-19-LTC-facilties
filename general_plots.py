 # -*- coding: utf-8 -*-
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

#files = os.listdir("Plots_specific")
# directory = "Plots_specific/"
# os.chdir(directory)







##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
#
#										Students
#
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################






# ##############################################################################################
# #										Student Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("MSI_outputs/Individually/MaskTypes/No_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Individually/MaskTypes/No_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]
# DI_mean_1 = df_mean_1['Daily Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']
# I_se_1 = df_se_1['Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Individually/MaskTypes/Cloth_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Individually/MaskTypes/Cloth_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']
# I_mean_2 = df_mean_2['Infected']
# I_se_2 = df_se_2['Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Individually/MaskTypes/Surgical_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Individually/MaskTypes/Surgical_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']
# I_mean_3 = df_mean_3['Infected']
# I_se_3 = df_se_3['Infected']

# df_mean_4 = pd.read_csv("MSI_outputs/Individually/MaskTypes/N95_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4 = pd.read_csv("MSI_outputs/Individually/MaskTypes/N95_mask/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4['Cumulative Infected'] = [df_mean_4['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4['Cumulative Infected']))]
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']
# I_mean_4 = df_mean_4['Infected']
# I_se_4 = df_se_4['Infected']


# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, ls='-.', c='grey', label='No Mask', marker='s', mfc='black', mec='black', ms=5, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, ls='-.', c='grey', label='Cloth Mask', marker='*', mfc='black', mec='black', ms=8, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='Medical Mask', marker='v', mfc='black', mec='black', ms=5, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, ls='-.', c='grey', label='N95 Mask', marker='x', mfc='black', mec='black', ms=5, mew=2, markevery=5)

# plt.xlabel('Number of Days', figure=fig1)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Class Modality=In-person classes',
# 					'Initial Infection=1% population',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Student Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Student Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Professor Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']



# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Instructor Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Instructor Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Instructor Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Student Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_0/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_0/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]
# DI_mean_1 = df_mean_1['Daily Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']
# I_se_1 = df_se_1['Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_1/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_1/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']
# I_mean_2 = df_mean_2['Infected']
# I_se_2 = df_se_2['Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_2/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_2/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']
# I_mean_3 = df_mean_3['Infected']
# I_se_3 = df_se_3['Infected']

# df_mean_4 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4['Cumulative Infected'] = [df_mean_4['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4['Cumulative Infected']))]
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']
# I_mean_4 = df_mean_4['Infected']
# I_se_4 = df_se_4['Infected']

# df_mean_5 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_4/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_5 = pd.read_csv("MSI_outputs/Individually/Masking/Compliance_4/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_5['Cumulative Infected'] = [df_mean_5['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_5['Cumulative Infected']))]
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']
# I_mean_5 = df_mean_5['Infected']
# I_se_5 = df_se_5['Infected']


# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, ls='-.', c='grey', label='0% Mask Compliance', marker='s', mfc='black', mec='black', ms=5, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, ls='-.', c='grey', label='25% Mask Compliance', marker='*', mfc='black', mec='black', ms=8, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='50% Mask Compliance', marker='v', mfc='black', mec='black', ms=5, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, ls='-.', c='grey', label='75% Mask Compliance', marker='x', mfc='black', mec='black', ms=5, mew=2, markevery=5)
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, ls='-.', c='grey', label='100% Mask Compliance', marker='o', mfc='black', mec='black', ms=5, mew=1, markevery=5)

# plt.xlabel('Number of Days', figure=fig1)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Class Modality=In-person classes',
# 					'Initial Infection=1% population',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Daily Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Hospitalized"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')




# fig4 = plt.figure()

# plt.errorbar(range(0,length), I_mean_1, 1.96*I_se_1, label='0% Mask Compliance')
# plt.errorbar(range(0,length), I_mean_2, 1.96*I_se_2, label='25% Mask Compliance')
# plt.errorbar(range(0,length), I_mean_3, 1.96*I_se_3, label='50% Mask Compliance')
# plt.errorbar(range(0,length), I_mean_4, 1.96*I_se_4, label='75% Mask Compliance')
# plt.errorbar(range(0,length), I_mean_5, 1.96*I_se_5, label='100% Mask Compliance')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active pool of Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')




# ##############################################################################################
# #										Instructor Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Instructor Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Instructor Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Instructor Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')









# ##############################################################################################
# #										Ventilation rate
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_2acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_2acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']


# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_3acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_3acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']


# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']


# df_mean_4 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_5acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_5acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']


# df_mean_5 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_6acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_6acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='2 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='3 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='4 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Ventilation Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='2 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='3 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='4 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Ventilation Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='2 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='3 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='4 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='5 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='5 air changes/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Ventilation Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Physical Distancing
# ##############################################################################################
# df_mean_1 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=2/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=2/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]

# DI_mean_1 = df_mean_1['Daily Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']
# I_se_1 = df_se_1['Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']
# I_mean_2 = df_mean_2['Infected']
# I_se_2 = df_se_2['Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=4/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=4/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']
# I_mean_3 = df_mean_3['Infected']
# I_se_3 = df_se_3['Infected']

# df_mean_4 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=5/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=5/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4['Cumulative Infected'] = [df_mean_4['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4['Cumulative Infected']))]
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']
# I_mean_4 = df_mean_4['Infected']
# I_se_4 = df_se_4['Infected']

# df_mean_5 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=6/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_5 = pd.read_csv("MSI_outputs/Individually/PhysicalDistancing/r=6/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_5['Cumulative Infected'] = [df_mean_5['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_5['Cumulative Infected']))]
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']
# I_mean_5 = df_mean_5['Infected']
# I_se_5 = df_se_5['Infected']


# length = 84
# fig1 = plt.figure()


# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, ls='-.', c='grey', label='Physical Distance=2 feet', marker='s', mfc='black', mec='black', ms=5, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, ls='-.', c='grey', label='Physical Distance=3 feet', marker='*', mfc='black', mec='black', ms=8, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='Physical Distance=4 feet', marker='v', mfc='black', mec='black', ms=5, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, ls='-.', c='grey', label='Physical Distance=5 feet', marker='x', mfc='black', mec='black', ms=5, mew=2, markevery=5)
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, ls='-.', c='grey', label='Physical Distance=6 feet', marker='o', mfc='black', mec='black', ms=5, mew=1, markevery=5)

# plt.xlabel('Number of Days', figure=fig1)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Class Modality=In-person classes',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Physical Distance=2 feet')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Physical Distance=3 feet')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Physical Distance=4 feet')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='Physical Distance=5 feet')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='Physical Distance=6 feet')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Daily Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Physical Distance=2 feet')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Physical Distance=3 feet')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Physical Distance=4 feet')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='Physical Distance=5 feet')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='Physical Distance=6 feet')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Hospitalized"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')




# fig4 = plt.figure()

# plt.errorbar(range(0,length), I_mean_1, 1.96*I_se_1, label='Physical Distance=2 feet')
# plt.errorbar(range(0,length), I_mean_2, 1.96*I_se_2, label='Physical Distance=3 feet')
# plt.errorbar(range(0,length), I_mean_3, 1.96*I_se_3, label='Physical Distance=4 feet')
# plt.errorbar(range(0,length), I_mean_4, 1.96*I_se_4, label='Physical Distance=5 feet')
# plt.errorbar(range(0,length), I_mean_5, 1.96*I_se_5, label='Physical Distance=6 feet')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active pool of Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Quanta rate
# ##############################################################################################
# df_mean_1 = pd.read_csv("14qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("14qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("48qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("48qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='14 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='48 quanta/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Quanta Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='14 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='48 quanta/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Quanta Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='14 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='48 quanta/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Quanta Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Class modality
# ##############################################################################################

# df_mean_1 = pd.read_csv("MSI_outputs/Individually/ClassModality/MaxSize_inf/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Individually/ClassModality/MaxSize_inf/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]
# DI_mean_1 = df_mean_1['Daily Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']
# I_se_1 = df_se_1['Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Individually/ClassModality/MaxSize_60/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Individually/ClassModality/MaxSize_60/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']
# I_mean_2 = df_mean_2['Infected']
# I_se_2 = df_se_2['Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Individually/ClassModality/MaxSize_30/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Individually/ClassModality/MaxSize_30/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']
# I_mean_3 = df_mean_3['Infected']
# I_se_3 = df_se_3['Infected']


# length = 84
# fig1 = plt.figure()


# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, ls='-.', c='grey', label='All classes are In-person', marker='o', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, ls='-.', c='grey', label='Classes with size < 60 students are In-person', marker='*', mfc='black', mec='black', ms=8, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='Classes with size < 30 students are In-person', marker='v', mfc='black', mec='black', ms=6, mew=1, markevery=5)


# plt.xlabel('Number of Days', figure=fig1)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Physical Distance=2 feet',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='All classes are In-person')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Classes with size < 60 students are In-person')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Classes with size < 30 students are In-person')
# # plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='Physical Distance=5 feet')
# # plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='Physical Distance=6 feet')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Daily Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Physical Distance=2 feet',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='All classes are In-person')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Classes with size < 60 students are In-person')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Classes with size < 30 students are In-person')
# # plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='Physical Distance=5 feet')
# # plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='Physical Distance=6 feet')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Hospitalized"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Physical Distance=2 feet',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')




# fig4 = plt.figure()

# plt.errorbar(range(0,length), I_mean_1, 1.96*I_se_1, label='All classes are In-person')
# plt.errorbar(range(0,length), I_mean_2, 1.96*I_se_2, label='Classes with size < 60 students are In-person')
# plt.errorbar(range(0,length), I_mean_3, 1.96*I_se_3, label='Classes with size < 30 students are In-person')
# # plt.errorbar(range(0,length), I_mean_4, 1.96*I_se_4, label='Physical Distance=5 feet')
# # plt.errorbar(range(0,length), I_mean_5, 1.96*I_se_5, label='Physical Distance=6 feet')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active pool of Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Physical Distance=2 feet',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Initially Infected Population
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")

# #df_se_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# S_mean_1 = df_mean_1['Spreader']
# I_mean_1 = df_mean_1['Infected']

# df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
# #df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# #DI_se_2 = df_se_2['Daily Infected']
# #CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# #H_se_2 = df_se_2['Hospitalized']
# S_mean_2 = df_mean_2['Spreader']
# I_mean_2 = df_mean_2['Infected']

# df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# #df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# #DI_se_3 = df_se_3['Daily Infected']
# #CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# #H_se_3 = df_se_3['Hospitalized']
# S_mean_3 = df_mean_3['Spreader']
# I_mean_3 = df_mean_3['Infected']

# df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# #df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# #DI_se_4 = df_se_4['Daily Infected']
# #CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# #H_se_4 = df_se_4['Hospitalized']
# S_mean_4 = df_mean_4['Spreader']
# I_mean_4 = df_mean_4['Infected']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_5.csv")
# #df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# #DI_se_3 = df_se_3['Daily Infected']
# #CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# #H_se_3 = df_se_3['Hospitalized']
# S_mean_5 = df_mean_5['Spreader']
# I_mean_5 = df_mean_5['Infected']

# df_mean_6 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_6.csv")
# #df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_6 = df_mean_6['Daily Infected']
# CI_mean_6 = df_mean_6['Cumulative Infected']
# #DI_se_4 = df_se_4['Daily Infected']
# #CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_6 = df_mean_6['Hospitalized']
# #H_se_4 = df_se_4['Hospitalized']
# S_mean_6 = df_mean_6['Spreader']
# I_mean_6 = df_mean_6['Infected']

# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()
# plt.plot(range(0,length), CI_mean_1, label='Initial Infection=0.1% CI')
# plt.plot(range(0,length), CI_mean_2, label='Initial Infection=0.5% CI')
# plt.plot(range(0,length), CI_mean_3, label='Initial Infection=1.0% CI')
# plt.plot(range(0,length), CI_mean_4, label='Initial Infection=2.0% CI')
# plt.plot(range(0,length), CI_mean_5, label='Initial Infection=5.0% CI')
# plt.plot(range(0,length), CI_mean_6, label='Initial Infection=10.0% CI')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Initial Infected Population on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()
# plt.plot(range(0,length), DI_mean_1, label='Initial Infection=0.1% DI')
# plt.plot(range(0,length), DI_mean_2, label='Initial Infection=0.5% DI')
# plt.plot(range(0,length), DI_mean_3, label='Initial Infection=1.0% DI')
# plt.plot(range(0,length), DI_mean_4, label='Initial Infection=2.0% DI')
# plt.plot(range(0,length), DI_mean_5, label='Initial Infection=5.0% DI')
# plt.plot(range(0,length), DI_mean_6, label='Initial Infection=10.0% DI')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Initial Infected Population on new Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()
# plt.plot(range(0,length), H_mean_1, label='Initial Infection=0.1% H')
# plt.plot(range(0,length), H_mean_2, label='Initial Infection=0.5% H')
# plt.plot(range(0,length), H_mean_3, label='Initial Infection=1.0% H')
# plt.plot(range(0,length), H_mean_4, label='Initial Infection=2.0% H')
# plt.plot(range(0,length), H_mean_5, label='Initial Infection=5.0% H')
# plt.plot(range(0,length), H_mean_6, label='Initial Infection=10.0% H')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Initial Infected Population on new Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')


# fig4 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), S_mean_1, label='Initial Infection=0.1% S')
# plt.plot(range(0,length), S_mean_2, label='Initial Infection=0.5% S')
# plt.plot(range(0,length), S_mean_3, label='Initial Infection=1.0% S')
# plt.plot(range(0,length), S_mean_4, label='Initial Infection=2.0% S')
# plt.plot(range(0,length), S_mean_5, label='Initial Infection=5.0% S')
# plt.plot(range(0,length), S_mean_6, label='Initial Infection=10.0% S')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Impact of different Initial Infected Population on active Infection Spreaders"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')


# fig5 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_1, label='Initial Infection=0.1% I')
# plt.plot(range(0,length), I_mean_2, label='Initial Infection=0.5% I')
# plt.plot(range(0,length), I_mean_3, label='Initial Infection=1.0% I')
# plt.plot(range(0,length), I_mean_4, label='Initial Infection=2.0% I')
# plt.plot(range(0,length), I_mean_5, label='Initial Infection=5.0% I')
# plt.plot(range(0,length), I_mean_6, label='Initial Infection=10.0% I')

# plt.xlabel('Num Days', figure=fig5)
# plt.ylabel('Num Students', figure=fig5)
# title = "Impact of different Initial Infected Population on active Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig5.savefig(title + '.png', bbox_inches='tight')




# ##############################################################################################
# #										Testing
# ##############################################################################################

# df_mean_1 = pd.read_csv("MSI_outputs/Individually/Testing/Static/TestCapacity=2000/Static_Test_Capacity_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Individually/Testing/Static/TestCapacity=2000/Static_Test_Capacity_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]
# DI_mean_1 = df_mean_1['Daily Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']
# I_se_1 = df_se_1['Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Individually/Testing/Static/TestCapacity=5000/Static_Test_Capacity_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Individually/Testing/Static/TestCapacity=5000/Static_Test_Capacity_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']
# I_mean_2 = df_mean_2['Infected']
# I_se_2 = df_se_2['Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Individually/Testing/Static/TestCapacity=10000/Static_Test_Capacity_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Individually/Testing/Static/TestCapacity=10000/Static_Test_Capacity_3/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']
# I_mean_3 = df_mean_3['Infected']
# I_se_3 = df_se_3['Infected']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, ls='-.', c='grey', label='Testing Capacity=2000', marker='o', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, ls='-.', c='grey', label='Testing Capacity=5000', marker='*', mfc='black', mec='black', ms=8, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='Testing Capacity=10000', marker='v', mfc='black', mec='black', ms=6, mew=1, markevery=5)


# plt.xlabel('Number of Days', figure=fig1)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Class Modality=In-person classes',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People + Contact Trace'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Testing Capacity=2000')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Testing Capacity=5000')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Testing Capacity=10000')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Daily Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People + Contact Trace'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Testing Capacity=2000')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Testing Capacity=5000')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Testing Capacity=10000')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Hospitalized"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People + Contact Trace'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')




# fig4 = plt.figure()

# plt.errorbar(range(0,length), I_mean_1, 1.96*I_se_1, label='Testing Capacity=2000')
# plt.errorbar(range(0,length), I_mean_2, 1.96*I_se_2, label='Testing Capacity=5000')
# plt.errorbar(range(0,length), I_mean_3, 1.96*I_se_3, label='Testing Capacity=10000')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active pool of Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People + Contact Trace'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Social Isolation
# ##############################################################################################

# df_mean_1 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=no/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=no/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']
# I_se_1 = df_se_1['Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=first_two/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=first_two/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']
# I_mean_2 = df_mean_2['Infected']
# I_se_2 = df_se_2['Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=first_two_and_middle_two/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=first_two_and_middle_two/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']
# I_mean_3 = df_mean_3['Infected']
# I_se_3 = df_se_3['Infected']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Social Isolation')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Social Isolation for week 1 and 2')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Social Isolation for week 1,2,6 and 7')


# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Cumulative Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Social Isolation')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Social Isolation for week 1 and 2')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Social Isolation for week 1,2,6 and 7')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Daily Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Social Isolation')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Social Isolation for week 1 and 2')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Social Isolation for week 1,2,6 and 7')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Hospitalized"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')




# fig4 = plt.figure()

# plt.errorbar(range(0,length), I_mean_1, 1.96*I_se_1, label='No Social Isolation')
# plt.errorbar(range(0,length), I_mean_2, 1.96*I_se_2, label='Social Isolation for week 1 and 2')
# plt.errorbar(range(0,length), I_mean_3, 1.96*I_se_3, label='Social Isolation for week 1,2,6 and 7')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active pool of Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')





##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
#
#										Instructors
#
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################









# ##############################################################################################
# #										Professor Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']



# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Instructor Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Instructor Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Instructor Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Student Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Student Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Student Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Student Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')











# ##############################################################################################
# #										Professor Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Instructor Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Instructor Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Instructor Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Student Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']

# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Student Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Student Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Student Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ###############################################################################################
# ##										Ventilation rate
# ###############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_2acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_2acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_3acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_3acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_5acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_5acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_6acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_6acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='2 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='3 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='4 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Ventilation Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='2 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='3 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='4 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Ventilation Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='2 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='3 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='4 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='5 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='5 air changes/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Ventilation Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')








# ##############################################################################################
# #										Student Density
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_15sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_15sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_20sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_20sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_30sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_30sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_35sqftpprofessor_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_35sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='15 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='25 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='30 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='35 sqft/student Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Student Density on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='15 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='25 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='30 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='35 sqft/student Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Student Density on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='15 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='25 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='30 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='35 sqft/student Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Student Density on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Quanta rate
# ##############################################################################################
# df_mean_1 = pd.read_csv("14qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("14qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("48qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("48qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']


# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='14 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='48 quanta/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Quanta Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='14 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='48 quanta/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Quanta Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='14 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='48 quanta/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Quanta Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')











##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
#
#										Policies
#
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################












# #############################################################################################
# #										No Policy
# #############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_38.01sqftpprofessor_4acph_airborne_60maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_38.01sqftpprofessor_4acph_airborne_60maxClassSize_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of No Mask Policy on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=No Mask',
# 					'Student Mask Compliance=0%',
# 					'Instructor Mask Type=No Mask',
# 					'Instructor Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=38.01 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max Offline Class Size=60'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of No Mask Policy on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=No Mask',
# 					'Student Mask Compliance=0%',
# 					'Instructor Mask Type=No Mask',
# 					'Instructor Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=38.01 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max Offline Class Size=60'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')


# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of No Mask Policy on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=No Mask',
# 					'Student Mask Compliance=0%',
# 					'Instructor Mask Type=No Mask',
# 					'Instructor Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=38.01 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max Offline Class Size=60'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')




























































































# ##############################################################################################
# #										Strict Policy
# ##############################################################################################
# #df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_se.csv")

# df_mean_0 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_0.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# # DI_mean_0 = df_mean_0['Daily Infected']
# CI_mean_0 = df_mean_0['Cumulative Infected']
# SI_mean_0 = df_mean_0['Symptomatic']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# # H_mean_0 = df_mean_0['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_0 = df_mean_0['Infected']

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# CI_mean_1 = df_mean_1['Cumulative Infected']
# SI_mean_1 = df_mean_1['Symptomatic']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# # H_mean_0 = df_mean_0['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']

# # df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
# # #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# # CI_mean_2 = df_mean_2['Cumulative Infected']
# # SI_mean_2 = df_mean_2['Symptomatic']
# # #DI_se_1 = df_se_1['Daily Infected']
# # #CI_se_1 = df_se_1['Cumulative Infected']
# # # H_mean_0 = df_mean_0['Hospitalized']
# # #H_se_1 = df_se_1['Hospitalized']
# # I_mean_2 = df_mean_2['Infected']


# # df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# # #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# # CI_mean_3 = df_mean_3['Cumulative Infected']
# # SI_mean_3 = df_mean_3['Symptomatic']
# # #DI_se_1 = df_se_1['Daily Infected']
# # #CI_se_1 = df_se_1['Cumulative Infected']
# # # H_mean_0 = df_mean_0['Hospitalized']
# # #H_se_1 = df_se_1['Hospitalized']
# # I_mean_3 = df_mean_3['Infected']

# # df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# # #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# # CI_mean_4 = df_mean_4['Cumulative Infected']
# # SI_mean_4 = df_mean_4['Symptomatic']
# # #DI_se_1 = df_se_1['Daily Infected']
# # #CI_se_1 = df_se_1['Cumulative Infected']
# # # H_mean_0 = df_mean_0['Hospitalized']
# # #H_se_1 = df_se_1['Hospitalized']
# # I_mean_4 = df_mean_4['Infected']

# length = 84
# fig1 = plt.figure()

# #plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
# plt.plot(range(0,length), CI_mean_0, label='Test Capacity=200')
# plt.plot(range(0,length), CI_mean_1, label='Test Capacity=500')
# # plt.plot(range(0,length), CI_mean_2, label='Outside Infection=25 people/day')
# # plt.plot(range(0,length), CI_mean_3, label='Outside Infection=50 people/day')
# # plt.plot(range(0,length), CI_mean_4, label='Outside Infection=100 people/day')
# # plt.plot(range(0,length), CI_mean_3, label='Class Fraction=25%')
# # plt.plot(range(0,length), CI_mean_4, label='Class Fraction=50%')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Cumulative Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30 students',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=100 people/day',
# 					'Initial Infection=1% population',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# #plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')
# plt.plot(range(0,length), I_mean_0, label='Test Capacity=200')
# plt.plot(range(0,length), I_mean_1, label='Test Capacity=500')
# # plt.plot(range(0,length), I_mean_2, label='Outside Infection=25 people/day')
# # plt.plot(range(0,length), I_mean_3, label='Outside Infection=50 people/day')
# # plt.plot(range(0,length), I_mean_4, label='Outside Infection=100 people/day')


# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Active Pool of Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30 students',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=100 people/day',
# 					'Initial Infection=1% population',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), SI_mean_0, label='Test Capacity=200')
# plt.plot(range(0,length), SI_mean_1, label='Test Capacity=500')
# # plt.plot(range(0,length), SI_mean_2, label='Outside Infection=25 people/day')
# # plt.plot(range(0,length), SI_mean_3, label='Outside Infection=50 people/day')
# # plt.plot(range(0,length), SI_mean_4, label='Outside Infection=100 people/day')


# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "New Symptomatic Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30 students',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=100 people/day',
# 					'Initial Infection=1% population',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')


# fig4 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), S_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), S_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), S_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), S_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), S_mean_4, label='Class Fraction=50%')


# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active Infection Spreaders"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')



# fig5 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), I_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), I_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), I_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), I_mean_4, label='Class Fraction=50%')

# plt.xlabel('Num Days', figure=fig5)
# plt.ylabel('Num Students', figure=fig5)
# title = "Pool of Active Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig5.savefig(title + '.png', bbox_inches='tight')

























# ##############################################################################################
# #										Strict Policy
# ##############################################################################################
# df_mean_1 = pd.read_csv("14 quantum per hour, Student with Strictest Mask - Short_mean.csv")
# df_se_1 = pd.read_csv("14 quantum per hour, Student with Strictest Mask - Short_se.csv")

# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']

# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']


# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')
# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')

# plt.xlabel('Num Days', figure=fig)
# plt.ylabel('Num Students', figure=fig)	 # EDIT NUM PEOPLE WITH INSTRUCTORS OR STUDENTS
# title = "Policy: Everyone wears medical mask"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Medical Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=Medical Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig.savefig(title + '.png', bbox_inches='tight')










##############################################################################################
#										Strict Policy
##############################################################################################
#df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")
#df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_se.csv")

# df_mean_0 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")
# ST_mean_0 = df_mean_0['Symptomatic Tests']
# PST_mean_0 = df_mean_0['Positive Symptomatic Tests']
# SI_mean_0 = df_mean_0['Symptomatic']
# AI_mean_0 = df_mean_0['Asymptomatic']
# CTT_mean_0 = df_mean_0['Contact Trace Tests']
# PCTT_mean_0 = df_mean_0['Positive Contact Trace Tests']
# ET_mean_0 = df_mean_0['Extra Tests']
# PET_mean_0 = df_mean_0['Positive Extra Tests']

# DI_mean_0 = df_mean_0['Daily Infected']
# CI_mean_0 = df_mean_0['Cumulative Infected']
# S_mean_0 = df_mean_0['Spreader']


# R_mean_0 = df_mean_0['Recovered']
# # #H_se_1 = df_se_1['Hospitalized']
# I_mean_0 = df_mean_0['Infected']

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# S_mean_1 = df_mean_1['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']

# df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
#df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# S_mean_2 = df_mean_2['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_2 = df_mean_2['Infected']


# df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# S_mean_3 = df_mean_3['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_3 = df_mean_3['Infected']

# df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# S_mean_4 = df_mean_4['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_4 = df_mean_4['Infected']

# length = 84
# fig1 = plt.figure()

# #plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
# plt.plot(range(0,length), ST_mean_0, label='Symptomatic Tests')
# plt.plot(range(0,length), SI_mean_0, label='Symptomatic Infected')
# plt.plot(range(0,length), PST_mean_0, label='Positive Symptomatic Tests')
# #plt.plot(range(0,length), AI_mean_0, label='Asymptomatic Infected')
# #plt.plot(range(0,length), CTT_mean_0, label='Contact Trace Tests')
# plt.plot(range(0,length), DI_mean_0, label='Daily New Infected')
# plt.plot(range(0,length), S_mean_0, label='Active Virus Spreaders')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Symptomatic Infected and Testing"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['No mask',
# 					'All In-person classes',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=16 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days',
# 					'Test Capacity=1000',
# 					'Test Type=MTest+(NCT)',
# 					'Contact Trace Test Type=Log-Infectability',
# 					'Non-Contact Trace Test Type=Log-Infectability'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# #plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')
# #plt.plot(range(0,length), ST_mean_0, label='Symptomatic Tests')
# #plt.plot(range(0,length), PST_mean_0, label='Positive Symptomatic Tests')
# #plt.plot(range(0,length), SI_mean_0, label='Symptomatic Infected')
# plt.plot(range(0,length), AI_mean_0, label='Asymptomatic Infected')
# plt.plot(range(0,length), CTT_mean_0, label='Contact Trace Tests/Symptomatic Class Tests')
# plt.plot(range(0,length), PCTT_mean_0, label='Positive Contact Trace Tests')
# plt.plot(range(0,length), DI_mean_0, label='Daily New Infected')
# plt.plot(range(0,length), S_mean_0, label='Active Virus Spreaders')


# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Contact Tracing and Testing"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['No mask',
# 					'All In-person classes',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=16 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days',
# 					'Test Capacity=1000',
# 					'Test Type=MTest+(NCT)',
# 					'Contact Trace Test Type=Log-Infectability',
# 					'Non-Contact Trace Test Type=Log-Infectability'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), AI_mean_0, label='Asymptomatic Infected')
# plt.plot(range(0,length), ET_mean_0, label='Asymptomatic Class Tests')
# plt.plot(range(0,length), PET_mean_0, label='Positive Asymptomatic Class Tests')
# plt.plot(range(0,length), DI_mean_0, label='Daily New Infected')
# plt.plot(range(0,length), S_mean_0, label='Active Virus Spreaders')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Asymptomatic Class Tests"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['No mask',
# 					'All In-person classes',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=16 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days',
# 					'Test Capacity=1000',
# 					'Test Type=MTest+(NCT)',
# 					'Contact Trace Test Type=Log-Infectability',
# 					'Non-Contact Trace Test Type=Log-Infectability'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')



# fig4 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_0, label='Active pool of Infected')
# plt.plot(range(0,length), CI_mean_0, label='Cumulative Infected')
# plt.plot(range(0,length), DI_mean_0, label='Daily Infected')
# plt.plot(range(0,length), R_mean_0, label='Recovered')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Infection Spread"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# textstr = '\n'.join(['No mask',
# 					'All In-person classes',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=16 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days',
# 					'Test Capacity=1000',
# 					'Test Type=MTest+(NCT)',
# 					'Contact Trace Test Type=Log-Infectability',
# 					'Non-Contact Trace Test Type=Log-Infectability'])

# # textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# # 					'Student Mask Compliance=100%',
# # 					'Instructor Mask Type=N95 Mask',
# # 					'Instructor Mask Compliance=100%',
# # 					'Ventilation Rate=4 air changes/hour',
# # 					'Student Density=78.15 sqft/student',
# # 					'Quanta Rate=20 quanta/hour',
# # 					'Initial Infection=1% population',
# # 					'Outside Infection=2 people/day',
# # 					'Max In-person Class Size=30',
# # 					'Testing Gap Days=3 days',
# # 					'Test Capacity=100',
# # 					'Test Type=Mtest',
# # 					'Contact Trace Sampling=Log of Infectability'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')



# # import matplotlib.pyplot as plt 
# # import numpy as np 
  
  
# # # Creating dataset 
# # np.random.seed(10) 
  
# # data_1 = np.random.normal(100, 10, 200) 
# # data_2 = np.random.normal(90, 20, 200) 
# # data_3 = np.random.normal(80, 30, 200) 
# # data_4 = np.random.normal(70, 40, 200) 
# # data = [data_1, data_2, data_3, data_4] 
  
# # fig = plt.figure(figsize =(10, 7)) 
  
# # # Creating axes instance 
# # ax = fig.add_axes([0, 0, 1, 1]) 
  
# # # Creating plot 
# # bp = ax.boxplot(data) 
  
# # # show plot 
# # plt.show() 





# ##############################################################################################
# #										Compounding Policies
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]

# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']

# # df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")
# # df_se_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se_1.csv")
# # DI_mean_2 = df_mean_2['Daily Infected']
# # CI_mean_2 = df_mean_2['Cumulative Infected']
# # DI_se_2 = df_se_2['Daily Infected']
# # CI_se_2 = df_se_2['Cumulative Infected']
# # H_mean_2 = df_mean_2['Hospitalized']
# # H_se_2 = df_se_2['Hospitalized']
# # I_mean_2 = df_mean_2['Infected']
# # I_se_2 = df_se_2['Infected']

# # df_mean_3 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=first_two_and_middle_two/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# # df_se_3 = pd.read_csv("MSI_outputs/Individually/SocialDistancing/weeks=first_two_and_middle_two/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# # DI_mean_3 = df_mean_3['Daily Infected']
# # CI_mean_3 = df_mean_3['Cumulative Infected']
# # DI_se_3 = df_se_3['Daily Infected']
# # CI_se_3 = df_se_3['Cumulative Infected']
# # H_mean_3 = df_mean_3['Hospitalized']
# # H_se_3 = df_se_3['Hospitalized']
# # I_mean_3 = df_mean_3['Infected']
# # I_se_3 = df_se_3['Infected']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
# # plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Physical Distancing + Mask Complaince')
# # plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Social Isolation for week 1,2,6 and 7')


# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Cumulative Infected"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Physical Distance=2 feet',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max In-person class size=30 students',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic Infected + Contact Tarce',
# 					'Testing Capacity=2000 tests/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')



# # #############################################################################################
# # 										Sunrise  Policy
# # #############################################################################################

# df_mean_0 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/no_policy/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_0 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/no_policy/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_0['Cumulative Infected'] = [df_mean_0['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_0['Cumulative Infected']))]
# CI_mean_0 = df_mean_0['Cumulative Infected']
# CI_se_0 = df_se_0['Cumulative Infected']

# df_mean_1 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]
# CI_mean_1 = df_mean_1['Cumulative Infected']
# CI_se_1 = df_se_1['Cumulative Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# CI_mean_2 = df_mean_2['Cumulative Infected']
# CI_se_2 = df_se_2['Cumulative Infected']


# df_mean_3 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/class_modality_physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/class_modality_physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# CI_mean_3 = df_mean_3['Cumulative Infected']
# CI_se_3 = df_se_3['Cumulative Infected']

# df_mean_4 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/testing_class_modality_physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/testing_class_modality_physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4['Cumulative Infected'] = [df_mean_4['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4['Cumulative Infected']))]
# CI_mean_4 = df_mean_4['Cumulative Infected']
# CI_se_4 = df_se_4['Cumulative Infected']

# df_mean_5 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/revised_class_modality_testing_physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_5 = pd.read_csv("MSI_outputs/Compounded/UMN_sunrise_policy/revised_class_modality_testing_physical_distancing_masking/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_5['Cumulative Infected'] = [df_mean_5['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_5['Cumulative Infected']))]
# CI_mean_5 = df_mean_5['Cumulative Infected']
# CI_se_5 = df_se_5['Cumulative Infected']


# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_0, 1.96*CI_se_0, ls='-.', c='grey', label='No Policy', marker='*', mfc='black', mec='black', ms=8, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, ls='-.', c='grey', label='Masking', marker='s', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, ls='-.', c='grey', label='Physical Distancing + Masking', marker='d', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='Class Modality + Physical Distancing + Masking', marker='2', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, ls='-.', c='grey', label='Testing + Class Modality +\nPhysical Distancing + Masking', marker='o', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_5, ls='-.', c='grey', label='Revised Class Modality + Testing +\nPhysical Distancing + Masking', marker='x', mfc='black', mec='black', ms=6, mew=1, markevery=5)

# plt.xlabel('Number of Days', figure=fig1)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)


# plt.legend(bbox_to_anchor=(0.33, 0.4), loc=2, borderaxespad=0., prop={'size': 10})

# textstr = '\n'.join(['Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic people'])
# #props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# #plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# fig1.set_figheight(8)
# fig1.set_figwidth(8)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')



# fig2 = plt.figure()

# #plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Masking')
# #plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Physical Distancing + Masking')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, ls='-.', c='grey', label='Class Modality +\nPhysical Distancing + Masking', marker='o', mfc='black', mec='black', ms=6, mew=1, markevery=5)
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, ls='-.', c='grey', label='Testing + Class Modality +\nPhysical Distancing + Masking', marker='x', mfc='black', mec='black', ms=6, mew=2, markevery=5)
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_5, ls='-.', c='grey', label='Revised Class Modality + \nTesting + Class Modality +\nPhysical Distancing + Masking', marker='^', mfc='black', mec='black', ms=6, mew=1, markevery=5)


# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Community Transmission Cumulative Infected 2"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing=Symptomatic People'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Individual(Testing)  Policy
# ##############################################################################################

# df_mean_0 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_0 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_0['Cumulative Infected'] = [df_mean_0['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_0['Cumulative Infected']))]
# CI_mean_0 = df_mean_0['Cumulative Infected'][83]
# CI_se_0 = df_se_0['Cumulative Infected']

# df_mean_1 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Random/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Random/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1['Cumulative Infected'] = [df_mean_1['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1['Cumulative Infected']))]
# CI_mean_1 = df_mean_1['Cumulative Infected'][83]
# CI_se_1 = df_se_1['Cumulative Infected']

# df_mean_2 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Infectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Infectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2['Cumulative Infected'] = [df_mean_2['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2['Cumulative Infected']))]
# CI_mean_2 = df_mean_2['Cumulative Infected'][83]
# CI_se_2 = df_se_2['Cumulative Infected']

# df_mean_3 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3['Cumulative Infected'] = [df_mean_3['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3['Cumulative Infected']))]
# CI_mean_3 = df_mean_3['Cumulative Infected'][83]
# CI_se_3 = df_se_3['Cumulative Infected']

# df_mean_4 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT+NCT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT+NCT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4['Cumulative Infected'] = [df_mean_4['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4['Cumulative Infected']))]
# CI_mean_4 = df_mean_4['Cumulative Infected'][83]
# CI_se_4 = df_se_4['Cumulative Infected']




# df_mean_0_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=5000/S/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_0_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_0_5000['Cumulative Infected'] = [df_mean_0_5000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_0_5000['Cumulative Infected']))]
# CI_mean_0_5000 = df_mean_0_5000['Cumulative Infected'][83]
# CI_se_0_5000 = df_se_0_5000['Cumulative Infected']

# df_mean_1_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=5000/S+CT_Random/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Random/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1_5000['Cumulative Infected'] = [df_mean_1_5000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1_5000['Cumulative Infected']))]
# CI_mean_1_5000 = df_mean_1_5000['Cumulative Infected'][83]
# CI_se_1_5000 = df_se_1_5000['Cumulative Infected']

# df_mean_2_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=5000/S+CT_Infectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Infectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2_5000['Cumulative Infected'] = [df_mean_2_5000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2_5000['Cumulative Infected']))]
# CI_mean_2_5000 = df_mean_2_5000['Cumulative Infected'][83]
# CI_se_2_5000 = df_se_2_5000['Cumulative Infected']

# df_mean_3_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=5000/S+CT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3_5000['Cumulative Infected'] = [df_mean_3_5000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3_5000['Cumulative Infected']))]
# CI_mean_3_5000 = df_mean_3_5000['Cumulative Infected'][83]
# CI_se_3_5000 = df_se_3_5000['Cumulative Infected']

# df_mean_4_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=5000/S+CT+NCT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4_5000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT+NCT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4_5000['Cumulative Infected'] = [df_mean_4_5000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4_5000['Cumulative Infected']))]
# CI_mean_4_5000 = df_mean_4_5000['Cumulative Infected'][83]
# CI_se_4_5000 = df_se_4_5000['Cumulative Infected']



# df_mean_0_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=10000/S/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_0_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_0_10000['Cumulative Infected'] = [df_mean_0_10000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_0_10000['Cumulative Infected']))]
# CI_mean_0_10000 = df_mean_0_10000['Cumulative Infected'][83]
# CI_se_0_10000 = df_se_0_10000['Cumulative Infected']

# df_mean_1_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=10000/S+CT_Random/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_1_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Random/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_1_10000['Cumulative Infected'] = [df_mean_1_10000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_1_10000['Cumulative Infected']))]
# CI_mean_1_10000 = df_mean_1_10000['Cumulative Infected'][83]
# CI_se_1_10000 = df_se_1_10000['Cumulative Infected']

# df_mean_2_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=10000/S+CT_Infectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_2_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_Infectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_2_10000['Cumulative Infected'] = [df_mean_2_10000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_2_10000['Cumulative Infected']))]
# CI_mean_2_10000 = df_mean_2_10000['Cumulative Infected'][83]
# CI_se_2_10000 = df_se_2_10000['Cumulative Infected']

# df_mean_3_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=10000/S+CT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_3_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_3_10000['Cumulative Infected'] = [df_mean_3_10000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_3_10000['Cumulative Infected']))]
# CI_mean_3_10000 = df_mean_3_10000['Cumulative Infected'][83]
# CI_se_3_10000 = df_se_3_10000['Cumulative Infected']

# df_mean_4_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=10000/S+CT+NCT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
# df_se_4_10000 = pd.read_csv("MSI_outputs/Testing/WHO/TestCapacity=2000/S+CT+NCT_LogOfInfectability/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize/20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_se.csv")
# df_mean_4_10000['Cumulative Infected'] = [df_mean_4_10000['Cumulative Infected'][i]-5*(i+1) for i in range(len(df_mean_4_10000['Cumulative Infected']))]
# CI_mean_4_10000 = df_mean_4_10000['Cumulative Infected'][83]
# CI_se_4_10000 = df_se_4_10000['Cumulative Infected']

# length = 84
# fig1 = plt.figure()

# # plt.errorbar(range(0,length), CI_mean_0, 1.96*CI_se_0, label='S')
# # plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='S + CT (R)')
# # plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='S + CT (I)')
# # plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='S + CT (log(I))')
# # plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='S + CT + NCT (log(I))')

# plt.plot(['S', 'S+CT(R)', 'S+CT(I)', 'S+CT(log(I))', 'S+CT+NCT(log(I))'], [CI_mean_0, CI_mean_1, CI_mean_2, CI_mean_3, CI_mean_4], label='Testing Capacity=2000')
# plt.plot(['S', 'S+CT(R)', 'S+CT(I)', 'S+CT(log(I))', 'S+CT+NCT(log(I))'], [CI_mean_0_5000, CI_mean_1_5000, CI_mean_2_5000, CI_mean_3_5000, CI_mean_4_5000], label='Testing Capacity=5000')
# plt.plot(['S', 'S+CT(R)', 'S+CT(I)', 'S+CT(log(I))', 'S+CT+NCT(log(I))'], [CI_mean_0_10000, CI_mean_1_10000, CI_mean_2_10000, CI_mean_3_10000, CI_mean_4_10000], label='Testing Capacity=10000')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Community Transmission Cumulative Infected"
# #plt.title(title)
# plt.grid(True)


# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=0%',
# 					'Instructor Mask Type=Medical Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Student Density=25 sqft/student',
# 					'Initial Infection=1% population',
# 					'Outside Infection=5 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# # fig1.set_figheight(12)
# # fig1.set_figwidth(12)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')



# ##############################################################################################
# #										Sunrise  Policy Validation
# ##############################################################################################

# df_mean_0 = pd.read_csv("Testing Validation - Sheet1.csv")
# A_WSP = df_mean_0['Weekly Student positive cases(Actual)']
# A_CWSP = df_mean_0['Cumulative weekly positive cases(Actual)']
# P_WSP = df_mean_0['Weekly student positive cases(Predicted)']
# P_CWSP = df_mean_0['Cumulative weekly positive cases(Predicted)']
# P_WSP_SE = df_mean_0['Standard error']
# P_CWSP_SE = df_mean_0['Cumulative(SE)']



# length = 12
# fig1 = plt.figure()

# plt.errorbar(range(1,length+1), A_WSP, ls='-.', c='grey', label='Actual weekly student\npositive test cases', marker='*', mfc='black', mec='black', ms=8, mew=1)
# plt.errorbar(range(1,length+1), P_WSP, 1.96*P_WSP_SE, ls='-.', c='grey', label='Predicted weekly student\npositive test cases', marker='s', mfc='black', mec='black', ms=6, mew=1)

# plt.xlabel('Num Weeks', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Actual and Predicted weekly student positive test cases"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 0.90), loc=2, borderaxespad=0., prop={'size': 12})

# textstr = '\n'.join(['Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=0.02% population',
# 					'Testing=Symptomatic people'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# fig1.set_figheight(8)
# fig1.set_figwidth(8)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')



# fig2 = plt.figure()

# plt.errorbar(range(1,length+1), A_CWSP, ls='-.', c='grey', label='Actual weekly\ncumulative student\npositive test cases', marker='*', mfc='black', mec='black', ms=8, mew=1)
# plt.errorbar(range(1,length+1), P_CWSP, 1.96*P_CWSP_SE, ls='-.', c='grey', label='Predicted weekly\ncumulative student\npositive test cases', marker='s', mfc='black', mec='black', ms=6, mew=1)

# plt.xlabel('Number of Weeks', figure=fig2)
# plt.ylabel('Cumulative Number of Infected Students', figure=fig2)
# title = "Actual and Predicted weekly cumulative student positive test cases"
# #plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 0.90), loc=2, borderaxespad=0., prop={'size': 12})

# textstr = '\n'.join(['Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=0.02% population',
# 					'Testing=Symptomatic people'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# # fig2.set_figheight(8)
# # fig2.set_figwidth(8)
# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')



# ##############################################################################################
# #										LTC Plots
# ##############################################################################################

# df_mean_0 = pd.read_csv("Outputs_temp_staff_0%/mean.csv")
# df_mean_1 = pd.read_csv("Outputs_temp_staff_2%/mean.csv")
# df_mean_2 = pd.read_csv("Outputs_temp_staff_10%/mean.csv")
# df_mean_3 = pd.read_csv("Outputs_temp_staff_50%/mean.csv")

# df_se_0 = pd.read_csv("Outputs_temp_staff_0%/se.csv")
# df_se_1 = pd.read_csv("Outputs_temp_staff_2%/se.csv")
# df_se_2 = pd.read_csv("Outputs_temp_staff_10%/se.csv")
# df_se_3 = pd.read_csv("Outputs_temp_staff_50%/se.csv")
# # df_mean_4 = pd.read_csv("Outputs_temp_staff_80%/mean.csv")
# CI0 = df_mean_0['Cumulative Infected']
# CI1 = df_mean_1['Cumulative Infected']
# CI2 = df_mean_2['Cumulative Infected']
# CI3 = df_mean_3['Cumulative Infected']

# CI0_se = df_se_0['Cumulative Infected']
# CI1_se = df_se_1['Cumulative Infected']
# CI2_se = df_se_2['Cumulative Infected']
# CI3_se = df_se_3['Cumulative Infected']
# # CI4 = df_mean_4['Cumulative Infected']

# length = 180
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI0, 1.96*CI0_se, label='Temp Staff 0%')
# plt.errorbar(range(0,length), CI1, 1.96*CI1_se, label='Temp Staff 2%')
# plt.errorbar(range(0,length), CI2, 1.96*CI2_se, label='Temp Staff 10%')
# plt.errorbar(range(0,length), CI3, 1.96*CI3_se, label='Temp Staff 50%')
# # plt.errorbar(range(0,length), CI4, label='Temp Staff 80%')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num People', figure=fig1)
# title = "Change in Cumulative infected people based on variable temporary staff"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 0.90), loc=2, borderaxespad=0., prop={'size': 12})

# # textstr = '\n'.join(['Ventilation Rate=4 air changes/hour',
# # 					'Quanta Rate=20 quanta/hour',
# # 					'Initial Infection=0.02% population',
# # 					'Testing=Symptomatic people'])
# # props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# # plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# # fig1.set_figheight(8)
# # fig1.set_figwidth(8)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')




# ##############################################################################################
# #										LTC Plots 2 single
# ##############################################################################################
# import numpy as np
# df0_mean_0 = pd.read_csv("Outputs_temp_staff_10%/facility_0/mean.csv")
# df1_mean_0 = pd.read_csv("Outputs_temp_staff_10%/facility_1/mean.csv")

# df0_se_0 = pd.read_csv("Outputs_temp_staff_10%/facility_0/se.csv")
# df1_se_0 = pd.read_csv("Outputs_temp_staff_10%/facility_1/se.csv")

# CI0 = df0_mean_0['Cumulative Infected']
# CI1 = df0_mean_0['Cumulative Infected Residents']
# CI2 = df0_mean_0['Cumulative Infected Staff']

# CI3 = df1_mean_0['Cumulative Infected']
# CI4 = df1_mean_0['Cumulative Infected Residents']
# CI5 = df1_mean_0['Cumulative Infected Staff']

# SI0 = df0_se_0['Cumulative Infected']
# SI1 = df0_se_0['Cumulative Infected Residents']
# SI2 = df0_se_0['Cumulative Infected Staff']

# SI3 = df1_se_0['Cumulative Infected']
# SI4 = df1_se_0['Cumulative Infected Residents']
# SI5 = df1_se_0['Cumulative Infected Staff']

# # CI0_se = df0_se_0['Cumulative Infected Residents']
# # CI1_se = df1_se_0['Cumulative Infected Staff']

# length = 180
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI0+CI3, 1.96*(SI0+SI3), label='Cumulative Infected')
# plt.errorbar(range(0,length), CI1+CI4, 1.96*(SI1+SI4), label='Cumulative Infected Residents')
# plt.errorbar(range(0,length), CI2+CI5, 1.96*(SI2+SI5), label='Cumulative Infected Staff')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num People', figure=fig1)
# title = "Cumulative infected when shared temp staff=10%"
# plt.title(title)
# plt.grid(True)
# plt.xticks(np.arange(0, 181, 30))
# #plt.yticks(np.arange(0, 101, 25))

# plt.legend(bbox_to_anchor=(1.05, 0.90), loc=2, borderaxespad=0., prop={'size': 12})

# textstr = '\n'.join(['Shared temp staff=10%',
# 					'Threshold Infection\nrate to quarantine\na facility=10%',
# 					'Facility infected=Facility 1',
# 					'Initial Infection=0.02% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# # fig1.set_figheight(8)
# # fig1.set_figwidth(8)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')




# ##############################################################################################
# #										LTC Plots multiple facilities
# ##############################################################################################

# df_mean_0 = pd.read_csv("Outputs_temp_staff_10%/facility_0/mean.csv")
# df_mean_1 = pd.read_csv("Outputs_temp_staff_10%/facility_1/mean.csv")
# #df_mean_2 = pd.read_csv("Outputs_temp_staff_10%/facility_2/mean.csv")

# df_se_0 = pd.read_csv("Outputs_temp_staff_10%/facility_0/se.csv")
# df_se_1 = pd.read_csv("Outputs_temp_staff_10%/facility_1/se.csv")
# #df_se_2 = pd.read_csv("Outputs_temp_staff_10%/facility_2/se.csv")

# CI0 = df_mean_0['Cumulative Infected']
# CI1 = df_mean_1['Cumulative Infected']
# #CI2 = df_mean_2['Cumulative Infected']

# CI0_se = df_se_0['Cumulative Infected']
# CI1_se = df_se_1['Cumulative Infected']
# #CI2_se = df_se_2['Cumulative Infected']

# length = 180
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI0, 1.96*CI0_se, label='Facility 1')
# plt.errorbar(range(0,length), CI1, 1.96*CI1_se, label='Facility 2')
# #plt.errorbar(range(0,length), CI2, 1.96*CI2_se, label='Facility 3')
# # plt.errorbar(range(0,length), CI4, label='Temp Staff 810%')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num People', figure=fig1)
# title = "Cumulative infected people in different facilities when temporary staff = 10%"
# plt.title(title)
# plt.grid(True)

# plt.legend(bbox_to_anchor=(1.05, 0.90), loc=2, borderaxespad=0., prop={'size': 12})

# # textstr = '\n'.join(['Ventilation Rate=4 air changes/hour',
# # 					'Quanta Rate=20 quanta/hour',
# # 					'Initial Infection=0.02% population',
# # 					'Testing=Symptomatic people'])
# # props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# # plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# # fig1.set_figheight(8)
# # fig1.set_figwidth(8)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


















# import pandas as pd
# import matplotlib.cm as cm
# import numpy as np
# import matplotlib.pyplot as plt

# def plot_clustered_stacked(dfall, labels=None, title="Cumulative infected people in different facilities with varying temporary staff when infection starts in facility 1",  H="/", **kwargs):
# 	"""Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
# 	labels is a list of the names of the dataframe, used for the legend
# 	title is a string for the title of the plot
# 	H is the hatch used for identification of the different dataframe"""

# 	n_df = len(dfall)
# 	n_col = len(dfall[0].columns) 
# 	n_ind = len(dfall[0].index)
# 	axe = plt.subplot(111)

# 	for df in dfall : # for each data frame
# 		axe = df.plot(kind="bar",
# 					linewidth=0,
# 					stacked=True,
# 					ax=axe,
# 					legend=False,
# 					grid=False,
# 					**kwargs)  # make bar plots

# 	h,l = axe.get_legend_handles_labels() # get the handles we want to modify
# 	for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
# 		for j, pa in enumerate(h[i:i+n_col]):
# 			for rect in pa.patches: # for each index
# 				rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
# 				rect.set_hatch(H * int(i / n_col)) #edited part     
# 				rect.set_width(1 / float(n_df + 1))

# 	axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
# 	axe.set_xticklabels(df.index, rotation = 0)
# 	axe.set_xlabel('Num Days')
# 	axe.set_ylabel('Cumulative Infected People')
# 	axe.set_title(title)

#     # Add invisible data to add another legend
# 	n=[]        
# 	for i in range(n_df):
# 		n.append(axe.bar(0, 0, color="gray", hatch=H * i))

# 	l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
# 	if labels is not None:
# 		l2 = plt.legend(n, labels, loc=[1.01, 0.1]) 
# 	axe.add_artist(l1)
# 	#plt.show()
	
# 	fig = axe.get_figure()
# 	# fig.set_figheight(8)
# 	# fig.set_figwidth(8)
# 	fig.savefig(title + '.png', bbox_inches='tight')
# 	#axe.savefig(title + '.png', bbox_inches='tight')
# 	return axe


# df1_mean_0 = pd.read_csv("Outputs_temp_staff_0%/facility_0/mean.csv")['Cumulative Infected']
# df1_mean_1 = pd.read_csv("Outputs_temp_staff_0%/facility_1/mean.csv")['Cumulative Infected']

# df2_mean_0 = pd.read_csv("Outputs_temp_staff_2%/facility_0/mean.csv")['Cumulative Infected']
# df2_mean_1 = pd.read_csv("Outputs_temp_staff_2%/facility_1/mean.csv")['Cumulative Infected']

# df3_mean_0 = pd.read_csv("Outputs_temp_staff_10%/facility_0/mean.csv")['Cumulative Infected']
# df3_mean_1 = pd.read_csv("Outputs_temp_staff_10%/facility_1/mean.csv")['Cumulative Infected']

# df4_mean_0 = pd.read_csv("Outputs_temp_staff_50%/facility_0/mean.csv")['Cumulative Infected']
# df4_mean_1 = pd.read_csv("Outputs_temp_staff_50%/facility_1/mean.csv")['Cumulative Infected']


# def get_matrix(ts):
# 	mat = []
# 	df_mean_0 = pd.read_csv("Outputs_temp_staff_"+ts+"/facility_0/mean.csv")['Cumulative Infected']
# 	df_mean_1 = pd.read_csv("Outputs_temp_staff_"+ts+"/facility_1/mean.csv")['Cumulative Infected']
# 	for day in [30,60,90,120,150,180]:
# 		row = [df_mean_0[day-1], df_mean_1[day-1]]
# 		mat.append(row)
# 	return mat

# # create fake dataframes
# df1 = pd.DataFrame(get_matrix("0%"),
# 					index=["30", "60", "90", "120", "150", "180"],
# 					columns=["Facility 1", "Facility 2"])
# df2 = pd.DataFrame(get_matrix("2%"),
# 					index=["30", "60", "90", "120", "150", "180"],
# 					columns=["Facility 1", "Facility 2"])
# df3 = pd.DataFrame(get_matrix("10%"),
# 					index=["30", "60", "90", "120", "150", "180"], 
# 					columns=["Facility 1", "Facility 2"])
# df4 = pd.DataFrame(get_matrix("50%"),
# 					index=["30", "60", "90", "120", "150", "180"], 
# 					columns=["Facility 1", "Facility 2"])

# # Then, just call :
# plot_clustered_stacked([df1, df2, df3, df4],["Temp Staff 0%", "Temp Staff 2%", "Temp Staff 10%", "Temp Staff 50%"])










# ##############################################################################################
# #										LTC Plots 2 Testing
# ##############################################################################################
# import numpy as np
# df_mean_0 = pd.read_csv("Outputs_testing/testing frequency=1/Outputs_temp_staff_2%/facility_1/mean.csv")
# df_mean_1 = pd.read_csv("Outputs_testing/testing frequency=3/Outputs_temp_staff_2%/facility_1/mean.csv")
# df_mean_2 = pd.read_csv("Outputs_testing/testing frequency=7/Outputs_temp_staff_2%/facility_1/mean.csv")

# df_se_0 = pd.read_csv("Outputs_testing/testing frequency=1/Outputs_temp_staff_2%/facility_1/se.csv")
# df_se_1 = pd.read_csv("Outputs_testing/testing frequency=3/Outputs_temp_staff_2%/facility_1/se.csv")
# df_se_2 = pd.read_csv("Outputs_testing/testing frequency=7/Outputs_temp_staff_2%/facility_1/se.csv")
# # df_mean_4 = pd.read_csv("Outputs_temp_staff_80%/mean.csv")
# CI0 = df_mean_0['Cumulative Infected']
# CI1 = df_mean_1['Cumulative Infected']
# CI2 = df_mean_2['Cumulative Infected']

# CI0_se = df_se_0['Cumulative Infected']
# CI1_se = df_se_1['Cumulative Infected']
# CI2_se = df_se_2['Cumulative Infected']
# # CI4 = df_mean_4['Cumulative Infected']


# # CI0_se = df0_se_0['Cumulative Infected Residents']
# # CI1_se = df1_se_0['Cumulative Infected Staff']

# length = 180
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI0, 1.96*CI0_se, label='testing frequency=1')
# plt.errorbar(range(0,length), CI1, 1.96*CI1_se, label='testing frequency=3')
# plt.errorbar(range(0,length), CI2, 1.96*CI2_se, label='testing frequency=7')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num People', figure=fig1)
# title = "Cumulative infected when shared temp staff=2%"
# plt.title(title)
# plt.grid(True)
# plt.xticks(np.arange(0, 181, 30))
# #plt.yticks(np.arange(0, 101, 25))

# plt.legend(bbox_to_anchor=(1.05, 0.90), loc=2, borderaxespad=0., prop={'size': 12})

# textstr = '\n'.join(['Shared temp staff=2%',
# 					'Threshold Infection\nrate to quarantine\na facility=5%',
# 					'Facility infected=Facility 1',
# 					'Initial Infection=0.02% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# # fig1.set_figheight(8)
# # fig1.set_figwidth(8)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Grid search plot
# ##############################################################################################

import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()

# temp_staff = [2,4,10,20]
# test_frequency = [1,3,7,14,30]
# turnaround_time = [0,1,2,3]
# fpr = [0,1,2,5,10,20]
# fnr = [0,2,5,10,20]
# quarantine_location = [2,5,10]
#
# temp_staff = [10]
# test_frequency = [3]
# turnaround_time = [0,1,2,3]
# # fnr = [0,2,5,10]
# fnr = [20]
# quarantine_location = [5]
#
# cum_inf = np.zeros([4,4])
#
# for i in range(len(fnr)):
# 	for j in range(len(turnaround_time)):
# 		for k in range(len(test_frequency)):
# 			for l in range(len(quarantine_location)):
# 				for m in range(len(temp_staff)):
# 					line1 = "Outputs/"+"fnr_"+str(fnr[i])+"/"+"tt_"+str(turnaround_time[j])+"/"+"tf_"+str(test_frequency[k])+"/"+"ql_"+str(quarantine_location[l])+"/"+"ts_"+str(temp_staff[m])
# 					a = pd.read_csv(line1+"/facility_0/mean.csv")['Cumulative Infected'][179]
# 					b = pd.read_csv(line1+"/facility_1/mean.csv")['Cumulative Infected'][179]
# 					cum_inf[i,j] = a+b
#
#
# fig1 = plt.figure()
# ax = sns.heatmap(cum_inf, xticklabels=turnaround_time, yticklabels=fnr, annot=True)
# plt.xlabel("Turnaround Time")
# plt.ylabel("False Negative Rate")
# plt.title("Cumulative Infected")
# textstr = '\n'.join(['Temp Staff=10%',
# 					'Test Frequency=3 days',
# 					'Quarantine Location=5%'])
# props = dict(boxstyle='round', facecolor='grey', alpha=0.15)
# plt.text(1.25, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# title = 'heatmap'
# fig1.savefig(title + '.png', bbox_inches='tight')

mean_fac_0_df = pd.read_csv("fnr_20/facility_0/mean.csv")
mean_fac_1_df = pd.read_csv("fnr_20/facility_1/mean.csv")
fig0 = plt.figure()
ax = sns.lineplot("Day","Recovered", data=mean_fac_0_df)
ax1 = sns.lineplot("Day","Recovered", data=mean_fac_1_df)
plt.xlabel("Num Days")
plt.ylabel("Num People")
plt.title("Cumulative Residents and Staff Recovered")
fig0.savefig("Recovered.png")
# fig1 = plt.figure()
#
#
#
# fig1.savefig("Facility_1.png")