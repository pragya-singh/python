def sanatize(test_string):
	splitter = ""
	if "-" in test_string:
		splitter = "-"
	elif ":" in test_string:
		splitter = ":"
	else:
		return test_string
	(mins, secs) = test_string.split(splitter)
	return mins+"."+secs

class Athelete:
	def __init__(self, name, dob=None, times=[]):
		self.name = name
		self.dob = dob
		self.times = times

	def top_performances(self):
		return sorted(set(sanatize(element) for element in self.times))[0:3]

def read_file(file_name):
	try:
		with open(file_name) as data:
			line = data.readline()
			temp_list = line.strip().split(",")
			return Athelete(temp_list.pop(0), temp_list.pop(0), temp_list)
	except IOError as err:
		print("File Error : "+str(err))
		return None

james = read_file("james2.txt")
print(james.name+"'s fastest time are:"+str(james.top_performances()))

julie = read_file("julie2.txt")
print(julie.name+"'s fastest time are:"+str(julie.top_performances()))

mikey = read_file("mikey2.txt")
print(mikey.name+"'s fastest time are:"+str(mikey.top_performances()))

sarah = read_file("sarah2.txt")
print(sarah.name+"'s fastest time are:"+str(sarah.top_performances()))