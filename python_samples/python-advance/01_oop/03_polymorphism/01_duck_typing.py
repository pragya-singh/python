# Polymorphism can be done in following ways
# - Duck Typing
# - Operator Overloading
# - Method Overloading
# - Method Overriding



class PyCharm:

	def execute(self):
		print('Auto Complete')
		print('Complile')
		print('Run')

class MyIde:

	def execute(self):
		print('Flavours')
		print('Auto Complete')
		print('Complile')
		print('Run')						

# This is a Duck Typing overriding.
# Reason, launch can take any ide object provided 
# it has execute() method.
# In Java we have to have an interface.
class Laptop:
	def launch(self, ide):
		ide.execute()

pyCharm = PyCharm()
myIde = MyIde()

l = Laptop()
l.launch(pyCharm)
print("========")
l.launch(myIde)
