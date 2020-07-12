"""
<Problem Statement> 
Read race timings of james,julie,mikey,sarah from corresponding input files. 
Print the top three performances of each.

<Working Description>
One line is read from all files which correspond to race-time values of each
player.
Each line is splitted by comma. Since comma separated values are not in proper
format(like contains - or : in between), hence making the values in proper 
format using the function sanatize.So each value after split is sanatized and 
then after sanatizing the new list created is sorted.
For each player, first three unique values are displayed from sorted list.

Note: A good example of list comprehension has been used here.
	  [sanatize(t) for t in james] => returns a list. it reduces quite
	  a good amount of code. General format is as follows:
	  
	  output_list = [function(element) for element in input_list] 

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

def top_three_items(time_list):
	unique_list=[]
	count=0
	for time in time_list:
		if time not in unique_list:
			unique_list.append(time)
			count=count+1
		if count == 3:
			break
	return unique_list
			
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
		james = sorted([sanatize(t) for t in james])
		julie = sorted([sanatize(t) for t in julie])
		mikey = sorted([sanatize(t) for t in mikey])
		sarah = sorted([sanatize(t) for t in sarah])
		top_three_performances_james=top_three_items(james)
		top_three_performances_julie=top_three_items(julie)
		top_three_performances_mikey=top_three_items(mikey)
		top_three_performances_sarah=top_three_items(sarah)				
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
