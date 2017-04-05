#randomly generate dnd 5e character sheet
#TODO: generate stats
#TODO: generate backstory
#TODO: generate to pdf filled character sheet
#TODO: generate starting weapons
#TODO: generate characters past first level

import random
import math
#race
race = None
#stats
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
#hp
hitPoints = 0
#speed
speed = 0
#proficencies
proficiencies = []
#age
age = 0
#alignment
alignment = None
#size(feet)
size = 0.0
#weight(pounds)
weight = 0.0
#features and traits 
featuresAndTraits = {}
#what tools you are proficient in
toolProficiencies = []
#languages known
languages = []
#all skills
skills = {"Athletics":0, "Acrobatics":0, "Sleight of Hand":0, "Stealth":0, "Arcana":0, "History":0, "Investigation":0, "Nature":0, "Religion":0, "Animal Handling":0, "Insight":0, "Medicine":0, "Perception":0, "Survival":0, "Deception":0, "Intimidation":0, "Performance":0, "Persuasion":0}




def alignmentPick(lawNeuCha,gooNeuEvi):
	global alignment
	mutant = random.uniform(0,1)
	if mutant < 0.1:
		lawNeuCha = ["Lawful", "Neutral", "Chaotic"]
		gooNeuEvi = ["Good", "Neutral", "Evil"]
	else:
		lawNeuCha = lawNeuCha
		gooNeuEvi = gooNeuEvi
	first = random.choice(lawNeuCha)
	second = random.choice(gooNeuEvi)
	alignment = " ".join((first,second))

def dwarf():
	global strength
	global dexterity
	global constitution
	global intelligence
	global wisdom
	global charisma
	global hitPoints
	global speed
	global proficiencies
	global age
	global size
	global weight
	global featuresAndTraits
	global languages
	global skills

	alignmentPick(["Lawful"],["Good"])
	race = "Dwarf"	
	age = random.randint(5,350) 
	size = (int(random.uniform(4.0,5.0)*100))/100.0
	speed = 25

	featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	featuresAndTraits["Dwarven Resilience"] = "Advantage on saving throws against poison and resistance to poison"
	featuresAndTraits["Stonecunning"] = "History checks against stone objects get double proficiency modifer"
	languages.extend(["Dwarvish","Common"])

	proficiencies.extend(["Battlexe", "Handaxe", "Light Hammer", "Warhammer"])

	constitution += 2

	subrace = random.randint(0,1)
	if subrace == 0:
		race = "Hill " + race
		wisdom += 1
		hitPoints += 1

	else:
		race = "Mountain " + race
		strength += 2
		proficiencies.append("Light Armor")
		proficiencies.append("Medium Armor")
	
	print race 
	print alignment

def elf():
	global strength
	global dexterity
	global constitution
	global intelligence
	global wisdom
	global charisma
	global hitPoints
	global speed
	global proficiencies
	global age
	global size
	global weight
	global featuresAndTraits
	global languages
	global skills

	alignmentPick(["Chaotic"],["Good"])
	race = "Elf"
	age = random.randint(5,750)
	size = (int(random.uniform(5.0,6.5)*100))/100.0
	speed = 30
	featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	featuresAndTraits["Keen Sense"] = "Proficiency in Perception"
	skills["Perception"] = 1
	featuresAndTraits["Fey Ancestry"] = "Advantage on saving throws against being charmed and magic cannot make you sleep"
	featuresAndTraits["Trance"] = "Elves don't sleep, they must meditate for 4 hours during a long rest"
	languages.extend(["Elvish", "Common"])

	dexterity += 2
	subrace = random.randint(0,2)
	if subrace == 0:
		race = "High " + race
		intelligence += 1
		proficiencies.extend(["Long Sword", "ShortSword", "Short Bow", "Long Bow"])
		#Add Cantrip mod
		#Add extra language option

	elif subrace == 1:
		race = "Wood " + race
		wisdom += 1
		proficiencies.extend(["Long Sword", "ShortSword", "Short Bow", "Long Bow"])
		speed = 35
		featuresAndTraits["Mask of the Wild"] = "You can attempt to hide when lightly obscured by nature."

	else :
		race = "Dark " + race + " (Drow)"
		charisma += 1
		alignmentPick(["Chaotic"],["Evil"])

		featuresAndTraits["Superior Dark Vision"] = "Range: 120 feet. See in dim light as bright light and dark light at dim light"
		featuresAndTraits["Sunlight Sensitivity"] = "Disadvange on perception checks and attack rolls in sunlight."
		proficiencies.extend(["Rapier", "ShortSword", "Hand Crossbow"])
		#Add Drow Magic trait

	print race 
	print alignment

def race():
	#race dic, if subrace then listing them else repeated
	#dragonborn has draconic ancestry
	races = {"dwarf":dwarf,"elf":elf}#, "halfling":halfling, "human":human,"dragonborn":dragonborn,"gnome":gnome,"halfelf":halfelf,"halforc":halforc,"tiefling":tiefling}
	ranRace = random.choice(races.values())
	ranRace()

race()

