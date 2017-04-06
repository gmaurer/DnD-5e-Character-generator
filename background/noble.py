import settings 
import random

def noble():
	settings.background = "Noble"
	#skills
	settings.skills["History"] = 1
	settings.skills["Persuasion"] = 1
	#random languages generator

	#tool proficiencies
	settings.toolProficiencies.extend(["Gaming Set"])
	#equipment
	settings.equipment["Signet Ring"] = 1
	settings.equipment["Scroll of Pedigree"] = 1
	settings.equipment["Fine Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 25