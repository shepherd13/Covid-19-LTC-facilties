from main import run
import os

f = open("parameters.txt")
a = f.read().split("\n")
f.close()

temp_staff = [4,10,20]
test_frequency = [1,3,7,14,30]
turnaround_time = [0,1,2,3]
fnr = [0,5,10,20]
quarantine_location = [2,5,10]


# line_1_part_2 = "tf_"
# line_1_part_3 = "tt_"
# line_1_part_4 = "fpr_"
# line_1_part_5 = "ql_"

line_1_part_1 = "Output Directory: "
line_7_part_1 = "TEMP_PERCENTAGE: "
line_25_part_1 = "Test Frequency: "
line_26_part_1 = "Test Result turnaround time: "
line_28_part_1 = "False Negative Rate: "
line_22_part_1 = "Quarantine Location Infecion Rate: "

for i in fnr:
	for j in turnaround_time:
		for k in test_frequency:
			for l in quarantine_location:
				for m in temp_staff:
					line1 = "Outputs/"+"fnr_"+str(i)+"/"+"tt_"+str(j)+"/"+"tf_"+str(k)+"/"+"ql_"+str(l)+"/"+"ts_"+str(m)
					os.makedirs(line1)
					line1 = line_1_part_1 + line1
					line7 = line_7_part_1 + str(m/100.0)
					line25 = line_25_part_1 + str(k)
					line26 = line_26_part_1 + str(j)
					line28 = line_28_part_1 + str(i/100.0)
					line22 = line_22_part_1 + str(l/100.0)
					a[0] = line1
					a[6] = line7
					a[24] = line25
					a[25] = line26
					a[27] = line28
					a[21] = line22
					#print(line1)
					f = open("parameters.txt",'w')
					f.write("\n".join(a))
					f.close()
					run()
