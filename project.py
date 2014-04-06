#n is number of players
n=18
players = [0]*n
import random


def round(players):
	#organizes players in a top down structure
	players.sort()
	players.reverse()
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
	print players

round(players)
round(players)
round(players)
round(players)