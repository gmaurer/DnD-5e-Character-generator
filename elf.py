import settings 
import random
from alignments import alignmentPick

def elf():

	alignmentPick(["Chaotic"],["Good"])
	settings.race = "Elf"
	settings.age = random.randint(5,750)
	settings.size = (int(random.uniform(5.0,6.5)*100))/100.0
	settings.speed = 30
	settings.weight = random.randint(90,200)

	settings.featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	settings.featuresAndTraits["Keen Sense"] = "Proficiency in Perception"
	settings.featuresAndTraits["Fey Ancestry"] = "Advantage on saving throws against being charmed and magic cannot make you sleep"
	settings.featuresAndTraits["Trance"] = "Elves don't sleep, they must meditate for 4 hours during a long rest"
	
	settings.skills["Perception"] = 1
	settings.languages.extend(["Elvish", "Common"])

	settings.dexterity += 2
	subrace = random.randint(0,2)
	if subrace == 0:
		settings.race = "High " + settings.race
		settings.intelligence += 1
		settings.proficiencies.extend(["Long Sword", "ShortSword", "Short Bow", "Long Bow"])
		#Add Cantrip mod
		#Add extra language option

	elif subrace == 1:
		settings.race = "Wood " + settings.race
		settings.wisdom += 1
		settings.proficiencies.extend(["Long Sword", "ShortSword", "Short Bow", "Long Bow"])
		settings.speed = 35
		settings.featuresAndTraits["Mask of the Wild"] = "You can attempt to hide when lightly obscured by nature."

	else :
		settings.race = "Dark " + settings.race + " (Drow)"
		settings.charisma += 1
		alignmentPick(["Chaotic"],["Evil"])

		settings.featuresAndTraits["Superior Dark Vision"] = "Range: 120 feet. See in dim light as bright light and dark light at dim light"
		settings.featuresAndTraits["Sunlight Sensitivity"] = "Disadvange on perception checks and attack rolls in sunlight."
		settings.proficiencies.extend(["Rapier", "ShortSword", "Hand Crossbow"])
		#Add Drow Magic trait

	