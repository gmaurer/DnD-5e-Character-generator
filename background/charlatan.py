import settings 
import random

def charlatan():
	settings.background = "Charlatan"
	#skills
	settings.skills["Deception"] = 1
	settings.skills["Sleight of Hand"] = 1
	#random languages

	#tool proficiencies
	settings.toolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
	#equipment
	settings.equipment["Disguise Kit"] = 1
	settings.equipment["Set of Weighted Die"] = 1
	settings.equipment["Fine Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 15