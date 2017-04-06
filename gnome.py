import settings 
import random
from alignments import alignmentPick

def gnome():

	alignmentPick(["Lawful","Chaotic"],["Good"])
	settings.race = "Gnome"	
	settings.age = random.randint(5,500) 
	settings.size = (int(random.uniform(3.0,4.0)*100))/100.0
	settings.speed = 25
	settings.weight = random.randint(30,50)

	settings.featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	settings.featuresAndTraits["Gnome Cunning"] = "Advantage on Wis, Int, Cha saving throws against magic."
	
	settings.languages.extend(["Gnomish","Common"])

	settings.intelligence += 2

	subrace = random.randint(0,1)
	if subrace == 0:
		settings.race = "Forest " + settings.race
		settings.dexterity += 1
		settings.featuresAndTraits["Natural Illusionist"] = "You know Minor Illusion cantrip.  Int is spellcasting ability."
		settings.featuresAndTraits["Speak with Small Beasts"] = "Through sounds and small gestures you can communicate simple ideas to Small or smaller beasts."

	else:
		settings.race = "Rock " + settings.race
		settings.constitution += 1
		settings.featuresAndTraits["Artificer's Lore"] = "twice proficiency bonus on History checks related to magic items, alchemical objects, or technological devices."
		settings.featuresAndTraits["Tinker"] = "Proficiency in Artisan Tools. 1 hour and 10gp to construct Tiny clockwork device (AC 5, 1 hp) either: Clockwork Toy, Fire Starter, Music Box."
		settings.toolProficiencies.append(["Artisan Tools"])

		
