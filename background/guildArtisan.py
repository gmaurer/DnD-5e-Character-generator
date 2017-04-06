import settings 
import random

def guildArtisan():
	settings.background = "Guild Artisan"
	#skills
	settings.skills["Insight"] = 1
	settings.skills["Persuasion"] = 1
	#random languages generator

	#tool proficiencies
	#make random artisan tools generator 
	settings.toolProficiencies.extend(["Artisan Tools"])
	#equipment
	settings.equipment["Artisan Tools"] = 1
	settings.equipment["Letter of Introduction from Guild"] = 1
	settings.equipment["Travelers Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 15