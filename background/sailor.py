import settings 
import random

def sailor():
	settings.background = "Sailor"
	#skills
	settings.skills["Athletics"] = 1
	settings.skills["Perception"] = 1
	#random languages generator

	#tool proficiencies
	settings.toolProficiencies.extend(["Navigators Tools", "Water Vehicles"])
	#equipment
	settings.equipment["Belaying Pin"] = 1
	settings.equipment["50 Foot Silk Rope"] = 1
	#lucky charm genreator
	settings.equipment["Lucky Charm"] = 1
	settings.equipment["Common Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 10