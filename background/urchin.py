import settings 
import random

def urchin():
	settings.background = "Urchin"
	#skills
	settings.skills["Sleight of Hand"] = 1
	settings.skills["Stealth"] = 1
	#random languages generator

	#tool proficiencies
	settings.toolProficiencies.extend(["Disguise Kit", "Thieves Tools"])
	#equipment
	settings.equipment["Small Knife"] = 1
	settings.equipment["Map of City"] = 1
	settings.equipment["Pet Mouse"] = 1
	settings.equipment["Token of Parents"] = 1
	settings.equipment["Common Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 10