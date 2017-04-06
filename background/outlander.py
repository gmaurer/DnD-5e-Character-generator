import settings 
import random

def outlander():
	settings.background = "Outlander"
	#skills
	settings.skills["Athletics"] = 1
	settings.skills["Survival"] = 1
	#random languages generator

	#tool proficiencies
	settings.toolProficiencies.extend(["Musical Instrument"])
	#equipment
	settings.equipment["A Staff"] = 1
	settings.equipment["Hunting Trap"] = 1
	#beast trophy generator file
	settings.equipment["Beast Trophy"] = 1
	settings.equipment["Travelers Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 10