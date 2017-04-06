import settings 
import random
from alignments import alignmentPick

def halfElf():

	alignmentPick(["Chaotic"],["Good","Neutral","Evil"])
	settings.race = "Half Elf"	
	settings.age = random.randint(5,200) 
	settings.size = (int(random.uniform(5.0,6.0)*100))/100.0
	settings.speed = 30
	settings.weight = random.randint(90,200)

	settings.featuresAndTraits["Dark Vision"] = "Range: 60 feet. See in dim light as bright light and dark light at dim light"
	settings.featuresAndTraits["Fey Ancestry"] = "Advantage on saving throws against being charmed and magic cannot put you to sleep."
	
	settings.languages.extend(["Elvish","Common"])
	#extra random language

	settings.charisma += 2
	abilityArray = [settings.strength, settings.dexterity, settings.constitution, settings.intelligence, settings.wisdom]
	abilityIncrease = random.randint(0,4)
	abilityArray[abilityIncrease] += 1
	del abilityArray[abilityIncrease]

	abilityIncrease = random.randint(0,3)
	abilityArray[abilityIncrease] += 1

	twoSkills = 0
	while True:

		skillPro = random.choice(settings.skills.keys()) 
		if settings.skills[skillPro] == 1:
			skillPro = random.choice(settings.skills.keys()) 
		else:
			if twoSkills == 2:
				break

			twoSkills += 1
			settings.skills[skillPro] = 1

