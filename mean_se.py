 # -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import glob
import scipy
from scipy import stats
import matplotlib.pyplot as plt

def updateCSV2(export, sus, inf, cumInf, cumInfRes, cumInfStaff, dailyInf, dailyInfRes, dailyInfStaff, inc, trans, sym, asym, rec, resrec, stafrec, dead, dailyTested, dailyTestedPos, dailyTestedNeg, cumTestedPos, quarantined, infFac, quarantinedFac):
    with open(export, 'w', newline='') as f:
        writer = csv.writer(f)

        l = []
        l.append('Day')
        l.append('Susceptible')
        l.append('Infected')
        l.append('Cumulative Infected')
        l.append('Cumulative Infected Residents')
        l.append('Cumulative Infected Staff')
        l.append('Daily Infected')
        l.append('Daily Infected Residents')
        l.append('Daily Infected Staff')
        l.append('Incubating')
        l.append('Transmitting')
        l.append('Symptomatic')
        l.append('Asymptomatic')
        l.append('Recovered')
        l.append('Residents Recovered')
        l.append('Staff Recovered')
        l.append('Dead')
        l.append('Daily Tested')
        l.append('Daily Tested Positive')
        l.append('Daily Tested Negative')
        l.append('Cumulative Tested Positive')
        l.append('Quarantined')
        l.append('Infected Facilities')
        l.append('Quarantined Facilities')
        writer.writerow(l)

        for i in range(len(sus)):
            l = []
            l.append(i)
            l.append(sus[i])
            l.append(inf[i])
            l.append(cumInf[i])
            l.append(cumInfRes[i])
            l.append(cumInfStaff[i])
            l.append(dailyInf[i])
            l.append(dailyInfRes[i])
            l.append(dailyInfStaff[i])
            l.append(inc[i])
            l.append(trans[i])
            l.append(sym[i])
            l.append(asym[i])
            l.append(rec[i])
            l.append(resrec[i])
            l.append(stafrec[i])
            l.append(dead[i])
            l.append(dailyTested[i])
            l.append(dailyTestedPos[i])
            l.append(dailyTestedNeg[i])
            l.append(cumTestedPos[i])
            l.append(quarantined[i])
            l.append(infFac[i])
            l.append(quarantinedFac[i])
            writer.writerow(l)

def get_mean_se(parameters, output_dir):
    directory = output_dir
    length = parameters['Days']
    file_names = glob.glob(directory + "/*.csv")

    List = []

    for file in file_names:
        # if len(file.split('/')[1]) > 6:
        #    continue
        df = pd.read_csv(file, skiprows=1)
        List.append(df)

    SusMat = []
    InfMat = []
    CumInfMat = []
    CumInfResMat = []
    CumInfStaffMat = []
    DailyInfMat = []
    DailyInfResMat = []
    DailyInfStaffMat = []
    num_incub = []
    TransMat = []
    SymMat = []
    AsymMat = []
    RecMat = []
    ResRecMat = []
    StafRecMat = []
    DeadMat = []
    DailyTestedMat = []
    DailyTestedPosMat = []
    DailyTestedNegMat = []
    CumTestedPosMat = []
    QuarantinedMat = []
    InfectedFacMat = []
    QuarantinedFacMat = []

    # Remove this part
    # a = 0
    #################


    for elem in List:
        # if elem['Cumulative Infected'].tolist()[-1] >= parameters['threshold']:
        #     a += 1

        SusMat.append(elem['Susceptible'].tolist())
        InfMat.append(elem['Infected'].tolist())
        CumInfMat.append(elem['Cumulative Infected'].tolist())
        CumInfResMat.append(elem['Cumulative Infected Residents'].tolist())
        CumInfStaffMat.append(elem['Cumulative Infected Staff'].tolist())
        DailyInfMat.append(elem['Daily Infected'].tolist())
        DailyInfResMat.append(elem['Daily Infected Residents'].tolist())
        DailyInfStaffMat.append(elem['Daily Infected Staff'].tolist())
        num_incub.append(elem['Incubating'].tolist())
        TransMat.append(elem['Transmitting'].tolist())
        SymMat.append(elem['Symptomatic'].tolist())
        AsymMat.append(elem['Asymptomatic'].tolist())
        RecMat.append(elem['Recovered'].tolist())
        ResRecMat.append(elem['Residents Recovered'].tolist())
        StafRecMat.append(elem['Staff Recovered'].tolist())
        DeadMat.append(elem['Dead'].tolist())
        DailyTestedMat.append(elem['Daily Tested'].tolist())
        DailyTestedPosMat.append(elem['Daily Tested Positive'].tolist())
        DailyTestedNegMat.append(elem['Daily Tested Negative'].tolist())
        CumTestedPosMat.append(elem['Cumulative Tested Positive'].tolist())
        QuarantinedMat.append(elem['Quarantined'].tolist())
        InfectedFacMat.append(elem['Infected Facilities'].tolist())
        QuarantinedFacMat.append(elem['Quarantined Facilities'].tolist())

    # print("Probability of intfection jump:", a/parameters['Runs'])

    SusMat = np.column_stack(tuple(SusMat))
    InfMat = np.column_stack(tuple(InfMat))
    CumInfMat = np.column_stack(tuple(CumInfMat))
    CumInfResMat = np.column_stack(tuple(CumInfResMat))
    CumInfStaffMat = np.column_stack(tuple(CumInfStaffMat))
    DailyInfMat = np.column_stack(tuple(DailyInfMat))
    DailyInfResMat = np.column_stack(tuple(DailyInfResMat))
    DailyInfStaffMat = np.column_stack(tuple(DailyInfStaffMat))
    num_incub = np.column_stack(tuple(num_incub))
    TransMat = np.column_stack(tuple(TransMat))
    SymMat = np.column_stack(tuple(SymMat))
    AsymMat = np.column_stack(tuple(AsymMat))
    RecMat = np.column_stack(tuple(RecMat))
    ResRecMat = np.column_stack(tuple(ResRecMat))
    StafRecMat = np.column_stack(tuple(StafRecMat))
    DeadMat = np.column_stack(tuple(DeadMat))
    DailyTestedMat = np.column_stack(tuple(DailyTestedMat))
    DailyTestedPosMat = np.column_stack(tuple(DailyTestedPosMat))
    DailyTestedNegMat = np.column_stack(tuple(DailyTestedNegMat))
    CumTestedPosMat = np.column_stack(tuple(CumTestedPosMat))
    QuarantinedMat = np.column_stack(tuple(QuarantinedMat))
    InfectedFacMat = np.column_stack(tuple(InfectedFacMat))
    QuarantinedFacMat = np.column_stack(tuple(QuarantinedFacMat))
    

    SusMat = SusMat.transpose()
    InfMat = InfMat.transpose()
    CumInfMat = CumInfMat.transpose()
    CumInfResMat = CumInfResMat.transpose()
    CumInfStaffMat = CumInfStaffMat.transpose()
    DailyInfMat = DailyInfMat.transpose()
    DailyInfResMat = DailyInfResMat.transpose()
    DailyInfStaffMat = DailyInfStaffMat.transpose()
    num_incub = num_incub.transpose()
    TransMat = TransMat.transpose()
    SymMat = SymMat.transpose()
    AsymMat = AsymMat.transpose()
    RecMat = RecMat.transpose()
    ResRecMat = ResRecMat.transpose()
    StafRecMat = StafRecMat.transpose()
    DeadMat = DeadMat.transpose()
    DailyTestedMat = DailyTestedMat.transpose()
    DailyTestedPosMat = DailyTestedPosMat.transpose()
    DailyTestedNegMat = DailyTestedNegMat.transpose()
    CumTestedPosMat = CumTestedPosMat.transpose()
    QuarantinedMat = QuarantinedMat.transpose()
    InfectedFacMat = InfectedFacMat.transpose()
    QuarantinedFacMat = QuarantinedFacMat.transpose()
    

    # get standard error
    semSus = scipy.stats.sem(SusMat)
    semInf = scipy.stats.sem(InfMat)
    semCumInf = scipy.stats.sem(CumInfMat)
    semCumInfRes = scipy.stats.sem(CumInfResMat)
    semCumInfStaff = scipy.stats.sem(CumInfStaffMat)
    semDailyInf = scipy.stats.sem(DailyInfResMat)
    semDailyInfRes = scipy.stats.sem(DailyInfStaffMat)
    semDailyInfStaff = scipy.stats.sem(DailyInfMat)
    semnum_incub = scipy.stats.sem(num_incub)
    semTransMat = scipy.stats.sem(TransMat)
    semSymMat = scipy.stats.sem(SymMat)
    semAsymMat = scipy.stats.sem(AsymMat)
    semRec = scipy.stats.sem(RecMat)
    semResRec = scipy.stats.sem(ResRecMat)
    semStafRec = scipy.stats.sem(StafRecMat)
    semDead = scipy.stats.sem(DeadMat)
    semDailyTested = scipy.stats.sem(DailyTestedMat)
    semDailyTestedPos = scipy.stats.sem(DailyTestedPosMat)
    semDailyTestedNeg = scipy.stats.sem(DailyTestedNegMat)
    semCumTestedPos = scipy.stats.sem(CumTestedPosMat)
    semQuarantined = scipy.stats.sem(QuarantinedMat)
    semInfectedFac = scipy.stats.sem(InfectedFacMat)
    semQuarantinedFac = scipy.stats.sem(QuarantinedFacMat)

    # get mean
    meanSus = SusMat.mean(0)
    meanInf = InfMat.mean(0)
    meanCumInf = CumInfMat.mean(0)
    meanCumInfRes = CumInfResMat.mean(0)
    meanCumInfStaff = CumInfStaffMat.mean(0)
    meanDailyInf = DailyInfMat.mean(0)
    meanDailyInfRes = DailyInfResMat.mean(0)
    meanDailyInfStaff = DailyInfStaffMat.mean(0)
    meannum_incub = num_incub.mean(0)
    meanTransMat = TransMat.mean(0)
    meanSymMat = SymMat.mean(0)
    meanAsymMat = AsymMat.mean(0)
    meanRec = RecMat.mean(0)
    meanResRec = ResRecMat.mean(0)
    meanStafRec = StafRecMat.mean(0)
    meanDead = DeadMat.mean(0)
    meanDailyTested = DailyTestedMat.mean(0)
    meanDailyTestedPos = DailyTestedPosMat.mean(0)
    meanDailyTestedNeg = DailyTestedNegMat.mean(0)
    meanCumTestedPos = CumTestedPosMat.mean(0)
    meanQuarantined = QuarantinedMat.mean(0)
    meanInfectedFac = InfectedFacMat.mean(0)
    meanQuarantinedFac = QuarantinedFacMat.mean(0)

    updateCSV2(directory + 'mean.csv', meanSus, meanInf, meanCumInf, meanCumInfRes, meanCumInfStaff,
                                    meanDailyInf, meanDailyInfRes, meanDailyInfStaff, meannum_incub, 
                                    meanTransMat, meanSymMat, meanAsymMat, meanRec, meanResRec, 
                                    meanStafRec, meanDead, meanDailyTested, meanDailyTestedPos, 
                                    meanDailyTestedNeg, meanCumTestedPos, meanQuarantined, meanInfectedFac, meanQuarantinedFac)
    updateCSV2(directory + 'se.csv', semSus, semInf, semCumInf, semCumInfRes, semCumInfStaff,
                                    semDailyInf, semDailyInfRes, semDailyInfStaff, semnum_incub, 
                                    semTransMat, semSymMat, semAsymMat, semRec, semResRec, semStafRec,
                                    semDead, semDailyTested, semDailyTestedPos, semDailyTestedNeg,
                                    semCumTestedPos, semQuarantined, semInfectedFac, semQuarantinedFac)
