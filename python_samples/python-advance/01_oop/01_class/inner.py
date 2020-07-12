
class Student:

	def __init__(self, name, age, lap):
		self.name = name
		self.age = age
		self.lap = lap

	def info(self):
		return f'{self.name} {self.age}'

	class Laptop:

		def __init__(self, brand, os):
			self.brand = brand
			self.os = os

		def show(self):
			return f'{self.brand} {self.os}'

if __name__ == "__main__":
	s1 = Student("Gaurav Singh", 22, Student.Laptop('Apple', 'MacOS'))
	s2 = Student("Jacob Sabastin", 21, Student.Laptop('Microsoft', 'Windows'))

	print(f'{s1.info()} {s1.lap.show()}')
	print(f'{s2.info()} {s2.lap.show()}')

