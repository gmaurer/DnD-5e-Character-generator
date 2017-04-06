import settings 
import random

def hermit():
	settings.background = "Hermit"
	#skills
	settings.skills["Medicine"] = 1
	settings.skills["Religion"] = 1
	#random languages generator

	#tool proficiencies
	settings.toolProficiencies.extend(["Herbalism Kit"])
	#equipment
	settings.equipment["Scroll case full of notes"] = 1
	settings.equipment["Winter Blanket"] = 1
	settings.equipment["Herbalism Kit"] = 1
	settings.equipment["Common Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 5