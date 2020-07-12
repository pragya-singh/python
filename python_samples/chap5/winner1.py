"""
<Problem Statement> 
Read race timings of james,julie,mikey,sarah from corresponding input files. 
Print the top three performances of each.

<Working Description>
Working of this is not different from winner.py. But two very important things
have been used here. set(list) and list[start,end].
For unique values set has been used => which has been sorted and then first three
values have been filtered from the outcome list.
"""
def sanatize(time_string):
	splitter=""
	if "-" in time_string:
		splitter = "-"
	elif ":" in time_string:
		splitter = ":"
	else:
		return(time_string)
	(mins,secs)=time_string.split(splitter)
	return(mins+"."+secs)
			
james=[]
julie=[]
mikey=[]
sarah=[]

try:
	with open("james.txt") as james_file, open("julie.txt") as julie_file, open("mikey.txt") as mikey_file, open("sarah.txt") as sarah_file:
		james_time_taken = james_file.readline()
		julie_time_taken = julie_file.readline()
		mikey_time_taken = mikey_file.readline()
		sarah_time_taken = sarah_file.readline() 
		james = james_time_taken.strip().split(",")
		julie = julie_time_taken.strip().split(",")
		mikey = mikey_time_taken.strip().split(",")
		sarah = sarah_time_taken.strip().split(",")
		top_three_performances_james = sorted(set([sanatize(t) for t in james]))[0:3]
		top_three_performances_julie = sorted(set([sanatize(t) for t in julie]))[0:3]
		top_three_performances_mikey = sorted(set([sanatize(t) for t in mikey]))[0:3]
		top_three_performances_sarah = sorted(set([sanatize(t) for t in sarah]))[0:3]			
		print(james)
		print(julie)
		print(mikey)
		print(sarah)
		print("TOP THREE PERFOROMANCES JAMES :"+str(top_three_performances_james))
		print("TOP THREE PERFOROMANCES JULIE :"+str(top_three_performances_julie))
		print("TOP THREE PERFOROMANCES MIKEY :"+str(top_three_performances_mikey))
		print("TOP THREE PERFOROMANCES SARAH :"+str(top_three_performances_sarah))
except IOError as err:
	print("File Error : "+str(err))
