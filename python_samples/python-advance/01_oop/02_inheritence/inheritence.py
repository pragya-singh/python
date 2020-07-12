class A:

	def __init__(self):
		print("A's Constructor")

	def feature1(self):
		print('feature1')

	def feature2(self):
		print('feature2')	

class B(A):

	def __init__(self):
		super().__init__()
		print("B's Constructor")

	def feature3(self):
		print('feature3')

	def feature4(self):
		print('feature4')

if __name__ == "__main__":
	
	a = A()
	b = B()

	b.feature1()
	b.feature2()
	b.feature3()
	b.feature4()
