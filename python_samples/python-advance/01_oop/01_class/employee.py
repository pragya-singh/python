class employee:

	def __init__(self, fname, lname, age):
		self.fname = fname
		self.lname = lname
		self.age = age


	def full_name(self):
		return f'{self.fname} {self.lname}'


if __name__ == "__main__":
	e1 = employee("Gaurav", "Singh", 33)
	e2 = employee("Jacob", "Orum", 36)

	print(e1.full_name())
	print(e2.full_name())