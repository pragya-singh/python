class stack:
	def __init__(self):
		self.container = []

	def push(self, o):
		self.container.append(o)

	def pop(self):
		return self.container.pop(-1)

	def top(self):
		return self.container[-1]

	def isEmpty(self):
		return len(self.container) == 0

if __name__ == "__main__":
	s = stack()
	print(s.isEmpty())
	s.push(1)
	print(s.top())
	s.push(2)
	print(s.top())
	s.pop()
	print(s.top())
	s.pop()
	print(s.isEmpty())

