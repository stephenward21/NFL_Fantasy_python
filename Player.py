class Player(object):
	def __init__(self, name, salary, strength, team):
		self.name = name
		self.salary = salary
		self.strength = strength
		self.team = team

	def print_player(self):
		print "Player: " + self.name
		print "TEAM: "  + self.team
		print "SALARY: " + str(self.salary)
		print "STRENGTH LEVEL: " + str(self.strength)

