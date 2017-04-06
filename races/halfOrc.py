import settings 
import random
from alignments import alignmentPick

def halfOrc():

	alignmentPick(["Chaotic"],["Neutral","Evil"])
	settings.race = "Half Orc"	
	settings.age = random.randint(5,75) 
	settings.size = (int(random.uniform(5.0,7.0)*100))/100.0
	settings.speed = 30
	settings.weight = random.randint(90,220)

	settings.featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	settings.featuresAndTraits["Menacing"] = "Proficient in Intimidation"
	settings.skills["Intimidation"] = 1
	settings.featuresAndTraits["Relentless Endurance"] = "When you are reduced to 0 HP, you go to 1 HP.  You can do this once per long rest."
	settings.featuresAndTraits["Savage Attacks"] = "When you roll a critical hitwith a melee weapon you add one extra damage dice to the damage dealt."

	settings.languages.extend(["Orc","Common"])
	#extra random language

	settings.strength += 2
	settings.constitution += 1


