#randomly generate dnd 5e character sheet
#TODO: generate stats
#TODO: generate backstory
#TODO: generate to pdf filled character sheet
#TODO: generate starting weapons
#TODO: generate characters past first level
#TODO: Attacks and weapons

import random
import math
import settings
from dwarf import dwarf
from elf import elf
from halfling import halfling
from human import human
from dragonborn import dragonborn
from gnome import gnome
from halfElf import halfElf


def race():
	#race dic, if subrace then listing them else repeated
	#dragonborn has draconic ancestry
	racesSelection = {"dwarf":dwarf,"elf":elf, "halfling":halfling, "human":human,"dragonborn":dragonborn,"gnome":gnome,"halfelf":halfElf}#,"halforc":halforc,"tiefling":tiefling}
	ranRace = random.choice(racesSelection.values())
	ranRace()
	print settings.race 
	print settings.alignment

settings.init()
race()

