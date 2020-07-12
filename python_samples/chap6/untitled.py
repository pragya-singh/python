class AtheleteList(list):
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.extend(times)

	def top3(self):
		return sorted(set([sanatize(t) for t in self]))[0:3]