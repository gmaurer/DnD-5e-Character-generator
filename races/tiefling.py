import settings 
import random
from alignments import alignmentPick

def tiefling():

	alignmentPick(["Chaotic"],["Neutral","Evil"])
	settings.race = "Tiefling"	
	settings.age = random.randint(5,120) 
	settings.size = (int(random.uniform(5.0,6.5)*100))/100.0
	settings.speed = 30
	settings.weight = random.randint(90,200)

	settings.featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	settings.featuresAndTraits["Hellish resistance"] = "Resistance to fire damage."
	settings.featuresAndTraits["Infernal Legacy"] = "You know Thaumaturgy cantrip. At level 3 you can cast Hellish Rebuke once per day as a second level spell. At 5th level you can cast Darkless once per day.  Charisma is your spellcasting ability."
	
	settings.languages.extend(["Infernal","Common"])
	#extra random language

	settings.charisma += 2
	settings.intelligence += 1


