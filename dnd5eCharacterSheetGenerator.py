#randomly generate dnd 5e character sheet
#TODO: generate stats
#TODO: generate backstory
#TODO: generate to pdf filled character sheet
#TODO: generate starting weapons
#TODO: generate characters past first level
#TODO: Attacks and weapons
#TODO: Name generator for each race

import random
import math
import settings
from races.dwarf import dwarf
from races.elf import elf
from races.halfling import halfling
from races.human import human
from races.dragonborn import dragonborn
from races.gnome import gnome
from races.halfElf import halfElf
from races.halfOrc import halfOrc
from races.tiefling import tiefling

def race():
	#race dic, if subrace then listing them else repeated
	#dragonborn has draconic ancestry
	racesSelection = {"dwarf":dwarf,"elf":elf, "halfling":halfling, "human":human,"dragonborn":dragonborn,"gnome":gnome,"halfelf":halfElf,"halforc":halfOrc}#,"tiefling":tiefling}
	ranRace = random.choice(racesSelection.values())
	ranRace()
	print settings.race 
	print settings.alignment

settings.init()
race()

