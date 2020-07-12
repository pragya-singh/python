# Generators and Yields are very important concept.
# It works similar to iterator but iterator is something 
# which eventually stores the all values in list/memory but 
# generator does not.

# Generators are achieved by having 'yield' in function. 'yield'
# is different from 'return' statement. It does not bring the cotrol
# out from function like 'return'. In case of yield the function state 
# is maintained and hence the value is returned one by one. 

# So Generators or yields are important for more efficient operation
# like not pulling huge list of result from DB and operate one by one. 
def topten():
	n = 1
	while n <= 10:
		yield n
		n += 1

class TopTen:

	def __init__(self):
		self.num = 1

	def get(self):
		while self.num <= 10:	
			yield self.num
			self.num += 1	


for i in topten():
	print(i)

for i in TopTen().get():
	print(i)	
