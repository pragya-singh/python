def sanatize(time_string):
	splitter=""
	if "-" in time_string:
		splitter = "-"
	elif ":" in time_string:
		splitter = ":"
	else:
		return time_string
	(mins,secs) = time_string.split(splitter)
	return mins+"."+secs
	
class AtheleteList(list):
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.extend(times)

	def top3(self):
		return sorted(set([sanatize(t) for t in self]))[0:3]