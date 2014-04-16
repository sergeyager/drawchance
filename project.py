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
		#print players
		players.sort()
		players.reverse()
		return players

class tournament:
	def __init__(self):
		#sets number of players and creates tournament roster
		n = 18
		self.players = [0]*n
	#this repeats the round and calculates the winner
	def start(self):
		x = round()
		for i in range(4):
			self.players = x.match(self.players)
		# finds if there is a clear winner after x rounds
	def winner(self):
		return self.players[0] == self.players[1]:


class simulation:
	#core to figuring out if a 5th round is needed
	def counter(self, tournaments):
		total = 0
		for i in range(tournaments):
			#create a fresh tournament roster for each trial
			t = tournament()
			#run an entire tournament for each trial
			t.start()
			# count if there is a clear winner, if no add 1
			if t.winner() == False:
				total += 1
		percentage = float(total)/float(tournaments) * 100
		print "The chance of a 5th round is " + str(percentage) + "%."

s = simulation()
s.counter(50000)
#t = tournament()
#t.play()

#if testing individual features, use t
#if testing for % of draw, use c
