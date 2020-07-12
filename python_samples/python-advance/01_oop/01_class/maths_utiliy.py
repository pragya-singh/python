class maths:

	@staticmethod
	def factorial(n):
		output = 1
		if n > 1:
			for i in range(1,n+1):
				output = output * i

		return output

	@staticmethod	
	def sum_n(n):
		return sum(list(range(1,n+1)))	
		
	@staticmethod	
	def sum_n2(n):
		l = list(range(1, n+1))	
		return sum([x**2 for x in l])

	@staticmethod	
	def sum_n3(n):
		l = list(range(1, n+1))
		return sum([x**3 for x in l])	
		
if __name__ == "__main__":

	print(maths.factorial(3))
	print(maths.sum_n(4))
	print(maths.sum_n2(4))
	print(maths.sum_n3(4))