import settings 
import random

def folkHero():
	settings.background = "Folk Hero"
	#skills
	settings.skills["Animal Handling"] = 1
	settings.skills["Survival"] = 1
	#random languages

	#tool proficiencies
	#make random artisan tools generator 
	settings.toolProficiencies.extend(["Artisan Tools","Land Vehicles"])
	#equipment
	settings.equipment["Artisan Tools"] = 1
	settings.equipment["Shovel"] = 1
	settings.equipment["Iron Pot"] = 1
	settings.equipment["Common Clothes"] = 1
	#wealth
	settings.wealth["Gold"] += 10