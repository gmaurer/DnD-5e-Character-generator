import settings 
import random
from alignments import alignmentPick

def human():

	alignmentPick(["Lawful", "Neutral", "Chaotic"],["Good", "Neutral", "Evil"])
	settings.race = "Human"	
	settings.age = random.randint(5,100) 
	settings.size = (int(random.uniform(5.0,7.0)*100))/100.0
	settings.speed = 30

	#TODO: add in human variant taking +1 to two scores and a feat and skill
	mutant = random.uniform(0,1)
	if mutant < 0.55:
		settings.strength += 1
		settings.dexterity += 1
		settings.constitution += 1
		settings.intelligence += 1
		settings.wisdom += 1
		settings.charisma += 1
	else:
		abilityArray = [settings.strength, settings.dexterity, settings.constitution, settings.intelligence, settings.wisdom, settings.charisma]
		abilityIncrease = random.randint(0,5)
		abilityArray[abilityIncrease] += 1
		del abilityArray[abilityIncrease]

		abilityIncrease = random.randint(0,4)
		abilityArray[abilityIncrease] += 1

		skillPro = random.choice(settings.skills.keys())
		settings.skills[skillPro] = 1





