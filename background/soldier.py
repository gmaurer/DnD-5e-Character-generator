import settings 
import random

def soldier():
	settings.background = "Soldier"
	#skills
	settings.skills["Athletics"] = 1
	settings.skills["Intimidation"] = 1
	#random languages generator

	#tool proficiencies
	settings.toolProficiencies.extend(["Gaming Set", "Land Vehicles"])
	#equipment
	settings.equipment["Rank Insignia"] = 1
	settings.equipment["Trophy from Enemy"] = 1
	settings.equipment["Gaming Set"] = 1
	settings.equipment["Common Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 10