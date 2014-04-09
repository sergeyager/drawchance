import random

class round:
	def match(self, players):
		#organizes players in a top down structure based on score
		for i in range(len(players)/2):
			#assigns players Win/Loss/Tie
			result = random.random()
			if result < 0.475:
				players[i*2+1] += 3
			elif result > 0.95:
				players[i*2+1] += 1
				players[i*2] += 1
			else:
				players[i*2] += 3
		#'bye' clause
		if len(players) % 2 != 0:
			players[-1] += 3
		print players
		players.sort()
		players.reverse()
		return players

class tournament:
	n = 18
	players = [0]*n
	#this repeats the round and calculates the winner
	def play(self):
		x = round()
		for i in range(4):
			self.players = x.match(self.players)
		# find winners
	def winner(self):
		if self.players[0] == self.players[1]:
			return False
		else:
			return True

class count:
	def counter(self, tournaments):
		total = 0
		t = tournament()
		for i in range(tournaments):
			t.play()
			# count if winners > 2
			if t.winner() == False:
				total += 1
		percentage = float(total)/float(tournaments) * 100
		print "The chance of a 5th round is " + str(percentage) + "%."

#c = count()
#c.counter(5)
t = tournament()
t.play()

