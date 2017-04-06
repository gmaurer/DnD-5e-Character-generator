import settings 
import random

def criminal():
	settings.background = "Criminal"
	#skills
	settings.skills["Deception"] = 1
	settings.skills["Stealth"] = 1
	#random languages

	#tool proficiencies
	#make random gaming set generator 
	settings.toolProficiencies.extend(["Gaming Set", "Thieves Tools"])
	#equipment
	settings.equipment["Crowbar"] = 1
	settings.equipment["Dark Common Clothes with Hood"] = 1
	#wealth
	settings.wealth["Gold"] += 15