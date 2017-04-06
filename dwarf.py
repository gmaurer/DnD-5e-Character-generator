import settings 
import random
from alignments import alignmentPick

def dwarf():

	alignmentPick(["Lawful"],["Good"])
	settings.race = "Dwarf"	
	settings.age = random.randint(5,350) 
	settings.size = (int(random.uniform(4.0,5.0)*100))/100.0
	settings.speed = 25
	settings.weight = random.randint(120,200)

	settings.featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	settings.featuresAndTraits["Dwarven Resilience"] = "Advantage on saving throws against poison and resistance to poison"
	settings.featuresAndTraits["Stonecunning"] = "History checks against stone objects get double proficiency modifer"
	
	settings.languages.extend(["Dwarvish","Common"])
	settings.proficiencies.extend(["Battlexe", "Handaxe", "Light Hammer", "Warhammer"])

	settings.constitution += 2

	subrace = random.randint(0,1)
	if subrace == 0:
		settings.race = "Hill " + settings.race
		settings.wisdom += 1
		settings.hitPoints += 1

	else:
		settings.race = "Mountain " + settings.race
		settings.strength += 2
		settings.proficiencies.append("Light Armor")
		settings.proficiencies.append("Medium Armor")


