class A:
	def show(self):
		print("I am in A")

# does not override the show() function
class B(A):
	pass

# show function is overridden 
class C(A):
	def show(self):
		print("I am in C")		


b = B()
c = C()

b.show()
c.show()