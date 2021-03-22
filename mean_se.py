 # -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import glob
import scipy
from scipy import stats
import matplotlib.pyplot as plt

def updateCSV2(export, sus, inf, cumInf, dailyInf, inc, trans, sym, asym, rec, resrec, stafrec, dead):
    with open(export, 'w', newline='') as f:
        writer = csv.writer(f)

        l = []
        l.append('Day')
        l.append('Susceptible')
        l.append('Infected')
        l.append('Cumulative Infected')
        l.append('Daily Infected')
        l.append('Incubating')
        l.append('Transmitting')
        l.append('Symptomatic')
        l.append('Asymptomatic')
        l.append('Recovered')
        l.append('Residents Recovered')
        l.append('Staff Recovered')
        l.append('Dead')
        writer.writerow(l)

        for i in range(len(sus)):
            l = []
            l.append(i)
            l.append(sus[i])
            l.append(inf[i])
            l.append(cumInf[i])
            l.append(dailyInf[i])
            l.append(inc[i])
            l.append(trans[i])
            l.append(sym[i])
            l.append(asym[i])
            l.append(rec[i])
            l.append(resrec[i])
            l.append(stafrec[i])
            l.append(dead[i])
            writer.writerow(l)

def get_mean_se(parameters):
    directory = parameters['Output Directory']
    length = parameters['Days']
    file_names = glob.glob(directory + "/*.csv")

    List = []

    for file in file_names:
        if len(file.split('/')[1]) > 6:
           continue
        df = pd.read_csv(file, skiprows=1)
        List.append(df)

    SusMat = []
    InfMat = []
    CumInfMat = []
    DailyInfMat = []
    num_incub = []
    TransMat = []
    SymMat = []
    AsymMat = []
    RecMat = []
    ResRecMat = []
    StafRecMat = []
    DeadMat = []

    for elem in List:
        SusMat.append(elem['Susceptible'].tolist())
        InfMat.append(elem['Infected'].tolist())
        CumInfMat.append(elem['Cumulative Infected'].tolist())
        DailyInfMat.append(elem['Daily Infected'].tolist())
        num_incub.append(elem['Incubating'].tolist())
        TransMat.append(elem['Transmitting'].tolist())
        SymMat.append(elem['Symptomatic'].tolist())
        AsymMat.append(elem['Asymptomatic'].tolist())
        RecMat.append(elem['Recovered'].tolist())
        ResRecMat.append(elem['Residents Recovered'].tolist())
        StafRecMat.append(elem['Staff Recovered'].tolist())
        DeadMat.append(elem['Dead'].tolist())


    SusMat = np.column_stack(tuple(SusMat))
    InfMat = np.column_stack(tuple(InfMat))
    CumInfMat = np.column_stack(tuple(CumInfMat))
    DailyInfMat = np.column_stack(tuple(DailyInfMat))
    num_incub = np.column_stack(tuple(num_incub))
    TransMat = np.column_stack(tuple(TransMat))
    SymMat = np.column_stack(tuple(SymMat))
    AsymMat = np.column_stack(tuple(AsymMat))
    RecMat = np.column_stack(tuple(RecMat))
    ResRecMat = np.column_stack(tuple(ResRecMat))
    StafRecMat = np.column_stack(tuple(StafRecMat))
    DeadMat = np.column_stack(tuple(DeadMat))
    

    SusMat = SusMat.transpose()
    InfMat = InfMat.transpose()
    CumInfMat = CumInfMat.transpose()
    DailyInfMat = DailyInfMat.transpose()
    num_incub = num_incub.transpose()
    TransMat = TransMat.transpose()
    SymMat = SymMat.transpose()
    AsymMat = AsymMat.transpose()
    RecMat = RecMat.transpose()
    ResRecMat = ResRecMat.transpose()
    StafRecMat = StafRecMat.transpose()
    DeadMat = DeadMat.transpose()
    

    # get standard error
    semSus = scipy.stats.sem(SusMat)
    semInf = scipy.stats.sem(InfMat)
    semCumInf = scipy.stats.sem(CumInfMat)
    semDailyInf = scipy.stats.sem(DailyInfMat)
    semnum_incub = scipy.stats.sem(num_incub)
    semTransMat = scipy.stats.sem(TransMat)
    semSymMat = scipy.stats.sem(SymMat)
    semAsymMat = scipy.stats.sem(AsymMat)
    semRec = scipy.stats.sem(RecMat)
    semResRec = scipy.stats.sem(ResRecMat)
    semStafRec = scipy.stats.sem(StafRecMat)
    semDead = scipy.stats.sem(DeadMat)


    # get mean
    meanSus = SusMat.mean(0)
    meanInf = InfMat.mean(0)
    meanCumInf = CumInfMat.mean(0)
    meanDailyInf = DailyInfMat.mean(0)
    meannum_incub = num_incub.mean(0)
    meanTransMat = TransMat.mean(0)
    meanSymMat = SymMat.mean(0)
    meanAsymMat = AsymMat.mean(0)
    meanRec = RecMat.mean(0)
    meanResRec = ResRecMat.mean(0)
    meanStafRec = StafRecMat.mean(0)
    meanDead = DeadMat.mean(0)


    updateCSV2(directory + 'mean.csv', meanSus, meanInf, meanCumInf, meanDailyInf, meannum_incub, meanTransMat, meanSymMat, meanAsymMat, meanRec, meanResRec, meanStafRec, meanDead)
    updateCSV2(directory + 'se.csv', semSus, semInf, semCumInf, semDailyInf, semnum_incub, semTransMat, semSymMat, semAsymMat, semRec, semResRec, semStafRec, semDead)
    #updateCSV2(directory + title + '_se.csv', semSus, semInf, semCumInf, semDailyInf, semnum_incub, semAsymMat, semSymMat,
    #    semRec, semDead, semDailyDead, semHosp, sembreathMat, semrespMat, semicuMat, semDailyTestedMat, semSpreaderMat, semQuarantinedMat,
    #    semSymptomaticTestsMat, semContactTraceTestsMat, semExtraTestsMat, semPositive_SymptomaticTestsMat, semPositive_ContactTraceTestsMat, semPositive_ExtraTestsMat)

    # fig = plt.figure()

    # plt.errorbar(range(0,length), meanSus, 1.96*semSus, label='Sus')
    # plt.errorbar(range(0,length), meanInf, 1.96*semInf, label='Inf')
    # plt.errorbar(range(0,length), meanRec, 1.96*semRec, label='Rec')
    # plt.errorbar(range(0,length), meannum_incub, 1.96*semnum_incub, label='Exp')
    # plt.errorbar(range(0,length), meanCumInf, 1.96*semCumInf, label='Total Inf')
    # #plt.errorbar(range(0,length), meanDailyTested, 1.96*semDailyTestedMat, label='Daily Tested')
    # #plt.errorbar(range(0,length), meanDead, 1.96*semDead, label='Dead')
    # #plt.errorbar(range(0,length), meanHosp, 1.96*semHosp, label='Hospitalized')
    # #plt.errorbar(range(0,length), meanDailyInf, 1.96*semDailyInf, label='Daily Infected')
    # #plt.errorbar(range(0,length), meanDailyDead, 1.96*semDailyDead, label='Daily Dead')
    # #plt.errorbar(range(0,length), meanAsymMat, 1.96*semAsymMat, label='Asymptomatic')
    # #plt.errorbar(range(0,length), meanSymMat, 1.96*semSymMat, label='Symptomatic')
    # plt.xlabel('Num Days', figure=fig)
    # plt.ylabel('Num People', figure=fig)
    # plt.title(title)

    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # #plt.show()
    # fig.savefig(directory + title + '_SEIR_Graph.png', bbox_inches='tight')

    #maX = max(meanInf)
    #day = np.where(meanInf == maX)
    #print(str(maX) + " people infected on day " + str(day[0][0]))
    #print(len(List))  # number of files tested