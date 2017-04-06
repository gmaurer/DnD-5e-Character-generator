import settings
import random
from proficiencyBonus import proficiencyBonus
from alignments import alignmentPick

def barbarian():
	selectSkills = ["Athletics", "Animal Handling", "Nature", "Perception", "Survival", "Intimidation"]

	settings.classes = "Barbarian"
	settings.level += 1	
	settings.barbarianLevel += 1
	settings.hitDice = 12
	settings.savingThrow["Strength"] = 1
	settings.savingThrow["Constitution"] = 1
	settings.proficiencies.extend(["Light Armor","Medium Armor","Shields","Simple Weapons","Martial Weapons"])
	settings.hitPoints = settings.hitDice + settings.abilityScoreModifier[settings.constitution]
	settings.rages = settings.ragesToLevel[settings.barbarianLevel][0]
	settings.rageBonus = settings.ragesToLevel[settings.barbarianLevel][1]

	counter = 0
	while counter < 2:
		skillPro = random.choice(selectSkills)
		if settings.skills[skillPro] == 0:
			settings.skills[skillPro] = 1
			counter += 1
		else: 
			skillPro = random.choice(settings.skills.keys())



	proficiencyBonus(settings.level)
