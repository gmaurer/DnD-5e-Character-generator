import settings 
import random

def proficiencyBonus(level):
	if 1 <= settings.level <= 4:
		settings.proficiencyBonus = 2
	elif 5 <= settings.level <= 8:
		settings.proficiencyBonus = 3
	elif 9 <= settings.level <= 12:
		settings.proficiencyBonus = 4
	elif 13 <= settings.level <= 16:
		settings.proficiencyBonus = 5
	elif 17 <= settings.level <= 20:
		settings.proficiencyBonus = 6
	else:
		settings.proficiencyBonus = 0