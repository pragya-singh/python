class game:
	player_count = 0

	def __init__(self):
		self.game_name = 'zoomanzi'
		self.players = []

	def subscribe(self, p):
		self.players.append(p)
		print(f'{p.name} subscribed to {self.game_name}')
		game.incr()

	@classmethod
	def incr(cls):
		cls.player_count += 1

class player:

	def __init__(self, g, name):
		self.name = name
		g.subscribe(self)
		

if __name__ == "__main__":
	g = game()
	p1 = player(g, "Gaurav Singh")
	p2 = player(g, "Ethen Hunt")
	print(game.player_count)
	
