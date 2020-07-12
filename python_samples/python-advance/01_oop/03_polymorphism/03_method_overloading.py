# There is no concept in Python to have direct method 
# overloading like in other langauges. 

# But we can implement method overloading like scenario
# in Python as well. As shown in sum function/method.

class Utility:
	
	@staticmethod
	def sum(a=None, b=None, c=None):
		
		s = 0
		if a != None and b != None and c != None:
			s = a + b + c
		elif a != None and b != None:
			s = a + b
		elif a != None:
			s = a	

		return s


print(Utility.sum(2,3,4))
print(Utility.sum(2,3))
print(Utility.sum(2))