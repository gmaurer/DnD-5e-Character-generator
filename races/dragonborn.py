import settings 
import random
from alignments import alignmentPick

def dragonborn():

	alignmentPick(["Lawful","Chaotic"],["Good", "Evil"])
	settings.race = "Dragonborn"	
	settings.age = random.randint(5,80) 
	settings.size = (int(random.uniform(6.0,8.0)*100))/100.0
	settings.speed = 30
	settings.weight = random.randint(200,300)

	settings.featuresAndTraits["Damage Resistance"] = "Resistance to damage of your Draconic Ancestry type."
	settings.featuresAndTraits["Breath Weapon"] = "Action: Exhale Draconic Ancestry attack.  DC = 8+Con+proficiency bonus."
	settings.featuresAndTraits["Draconic Ancestry"] = "Breath weapon type and damage resistance."


	settings.languages.extend(["Draconic","Common"])

	settings.strength += 2
	settings.charisma += 1

	subrace = random.randint(0,9)
	if subrace == 0 or subrace == 4:
		if subrace == 0:
			settings.race = "Black " + settings.race
			settings.featuresAndTraits["Acid Breath"] = "5 by 30 foot line (Dex save)"
		else:
			settings.race = "Copper " + settings.race
			settings.featuresAndTraits["Acid Breath"] = "5 by 30 foot line (Dex save)"

	elif subrace == 1 or subrace == 3:
		if subrace == 1:
			settings.race = "Blue " + settings.race
			settings.featuresAndTraits["Lightning Breath"] = "5 by 30 foot line (Dex save)"
		else:
			settings.race = "Bronze " + settings.race
			settings.featuresAndTraits["Lightning Breath"] = "5 by 30 foot line (Dex save)"
		
	elif subrace == 2 or subrace == 5 or subrace == 7:
		if subrace == 2:
			settings.race = "Brass " + settings.race
			settings.featuresAndTraits["Fire Breath"] = "5 by 30 foot line (Dex save)"
		elif subrace == 5:
			settings.race = "Gold " + settings.race
			settings.featuresAndTraits["Fire Breath"] = "15 foot cone (Dex save)"
		else:
			settings.race = "Red " + settings.race
			settings.featuresAndTraits["Fire Breath"] = "15 foot cone (Dex save)"
		
	elif subrace == 8 or subrace == 9:
		if subrace == 8:
			settings.race = "Silver " + settings.race
			settings.featuresAndTraits["Cold Breath"] = "15 foot cone (Con save)"
		else:
			settings.race = "White " + settings.race
			settings.featuresAndTraits["Cold Breath"] = "15 foot cone (Con save)"
		
	else:
		settings.race = "Green " + settings.race
		settings.featuresAndTraits["Poison Breath"] = "15 foot cone (Con save)"
		


