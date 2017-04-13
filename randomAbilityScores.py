import settings
import random

def randomAbilityScores():
	
	#abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
	abiltiyScoreTotal = 0
	#creates 4 ability scores

	for x in xrange(0,6):
		randomDice = []
		abiltiyScoreTotal = 0
		for y in xrange(0,4):
			randomDice.append(random.randint(1,6))
			
			
		for z in xrange(0,3):
			abiltiyScoreTotal += max(randomDice)
			del randomDice[randomDice.index(max(randomDice))]

		if x == 0:
			settings.strength += abiltiyScoreTotal
		elif x == 1:
			settings.dexterity += abiltiyScoreTotal
		elif x == 2:
			settings.constitution += abiltiyScoreTotal
		elif x == 3:
			settings.intelligence += abiltiyScoreTotal
		elif x == 4:
			settings.wisdom += abiltiyScoreTotal
		elif x == 5:
			settings.charisma += abiltiyScoreTotal

		







