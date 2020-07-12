# Operator Overloading

# There are multiple kinds of operators in Python
# For example : +, -, /, * etc. But what happens 
# behind the scene is there is function called for 
# every such operator. Like __add__, __sub__, __div__
# __mul__ etc. These are called "Magic Functions".

# We can also apply such kinds of operators for our 
# objects by overriding the Magic Functions which is
# called Operator overloading.

class Complex:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		x_new = self.x + other.x
		y_new = self.y + other.y	
		return Complex(x_new, y_new)

	def __eq__(self, other):	
		return (self.x == other.x) and (self.y == other.y)

	def __str__(self):
		return f"{self.x}+{self.y}i"

if __name__ == "__main__":
	
	c1 = Complex(2,3)
	c2 = Complex(4,5)

	# Applying '+' operator on Complex Numbers is possible
	# due to Operator overloading
	c = c1+c2
	print(c)

	# Comparing two complex numbers using '==' is possible
	# due to Operator overloading
	if c1 == c2:
		print("Equal")
	else:
		print("Unequal")

	c3 = Complex(2, 3)
	# Comparing two complex numbers using '==' is possible
	# due to Operator overloading		
	if c1 == c3:
		print("Equal")
	else:
		print("Unequal")			


