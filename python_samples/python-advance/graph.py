class graph:
	def __init__(self):
		self.l = {}

	def add(self, n, adjacent):
		self.l[n] = adjacent
		for node in adjacent:
			if node not in self.l:
				self.l[node] = [n]
			else:
				if n not in self.l[node]:
					self.l[node].append(n)

	def __str__(self):
		return str(self.l)

if __name__ == "__main__":
	g = graph()
	g.add(0, [1, 2, 3])
	g.add(1, [2, 3, 0])
	g.add(2, [3, 0, 1])
	g.add(3, [0, 1, 2])
	print(g)

