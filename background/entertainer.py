import settings 
import random

def entertainer():
	settings.background = "Entertainer"
	#skills
	settings.skills["Acrobatics"] = 1
	settings.skills["Performance"] = 1
	#random languages

	#tool proficiencies
	#make random music instrument generator 
	settings.toolProficiencies.extend(["Disguise Kit", "Musical Instrument"])
	#equipment
	settings.equipment["Musical Instrument"] = 1
	#create favor of admiror
	settings.equipment["Favor of an admiror"] = 1
	settings.equipment["Costume"] = 1
	#wealth
	settings.wealth["Gold"] += 15