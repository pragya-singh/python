def sanatize(time_string):
	splitter = ""
	if "-" in time_string:
		splitter = "-"
	elif ":" in time_string:
		splitter = ":"
	else:
		return time_string
	(mins,secs) = time_string.split(splitter)
	return mins+","+secs

def read_file(file_name):
	try:
		with open(file_name) as data:
			line = data.readline()
			return line.strip().split(",")
	except IOError as err:
		print("File Error : "+str(err))
		return None

def read_file_player(file_name):
	try:
		with open(file_name) as data:
			line = data.readline()
			temp_list = line.strip().split(",")
			return {"name":temp_list.pop(0),
					"dob":temp_list.pop(0),
					"times":sorted(set([sanatize(ele) for ele in temp_list]))[0:3]}
	except IOError as err:
		print("File Error : "+str(err))

sarah = read_file("sarah2.txt")
#(sarah_name,sarah_dob) = sarah.pop(0), sarah.pop(0)
#print(sorted(set([sanatize(t) for t in sarah]))[0:3])
sarah_data = {}
sarah_data['name'] = sarah.pop(0)
sarah_data['dob']  = sarah.pop(0)
sarah_data['times'] = sarah
print(sarah_data['name']+"'s fastest time are:"+str(sorted(set([sanatize(element) for element in sarah_data['times']]))[0:3])) 

james = read_file_player("james2.txt")
print(james['name']+"'s fastest time are:"+str(james["times"]))

