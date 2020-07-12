class A:

	def __init__(self):
		print("A's constructor")

	def feature1(self):
		print("feature1")	

class B:

	def __init__(self):
		print("B's constructor")

	def feature2(self):
		print("feature2")

# Constructor Behaviour in Inheritence
# Method Resolution Order(MRO)
# Interpretor first looks constructor for the 
# original class, then for left most Super Class.
# Hence Order is defined from Left to Right
class C(A,B):

	def __init__(self):
		super().__init__()
		print("C's constructor")

	def feature3(self):
		print("feature3")

if __name__ == "__main__":

	c = C()
	c.feature1()
	c.feature2()
	c.feature3()


