import settings 
import random
from alignments import alignmentPick

def halfling():

	alignmentPick(["Lawful"],["Good"])
	settings.race = "Halfling"
	settings.age = random.randint(5,150)
	settings.size = (int(random.uniform(2.5,3.5)*100))/100.0
	settings.speed = 25

	settings.featuresAndTraits["Lucky"] = "Reroll nautural 1's on attack, ability checks, or saving throws."
	settings.featuresAndTraits["Brave"] = "Advantage on saving throws against being frightened."
	settings.featuresAndTraits["Halfling Nimbleness"] = "You can move through the space of any creature that is a size larger than you."

	settings.languages.extend(["Halfling","Common"])

	settings.dexterity += 2

	subrace = random.randint(0,1)
	if subrace == 0:
		settings.race = "Lightfoot " + settings.race
		settings.charisma += 1 
		settings.featuresAndTraits["Naturally Stealthy"] = "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."

	else:
		settings.race = "Stout " + settings.race
		settings.constitution += 1 
		settings.featuresAndTraits["Stout Resilience"] = "Advantage on saving throws against poison and resistance against poison damage."
