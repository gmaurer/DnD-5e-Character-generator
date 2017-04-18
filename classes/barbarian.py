import settings
import random
from proficiencyBonus import proficiencyBonus
from alignments import alignmentPick

def barbarian():
	archetype = None

	selectSkills = ["Athletics", "Animal Handling", "Nature", "Perception", "Survival", "Intimidation"]
	settings.classes = "Barbarian"
	settings.level += 1	
	settings.barbarianLevel += 1
	settings.hitDice = 12
	settings.savingThrow["Strength"] = 1
	settings.savingThrow["Constitution"] = 1
	settings.proficiencies.extend(["Light Armor","Medium Armor","Shields","Simple Weapons","Martial Weapons"])
	settings.hitPoints = settings.hitDice + settings.abilityScoreModifier[settings.constitution]
	settings.rages = settings.ragesToLevel[settings.barbarianLevel][0]
	settings.rageBonus = settings.ragesToLevel[settings.barbarianLevel][1]
	settings.AC = 10 + settings.abilityScoreModifier[settings.dexterity] + settings.abilityScoreModifier[settings.constitution]
	settings.featuresAndTraits["UnArmored Defense"] = "Without Armor your AC is 10 + Dex + Con"

	counter = 0
	while counter < 2:
		skillPro = random.choice(selectSkills)
		if settings.skills[skillPro] == 0:
			settings.skills[skillPro] = 1
			counter += 1
		else: 
			skillPro = random.choice(settings.skills.keys())

	settings.barbarianLevel = 20
	for x in xrange(0,settings.barbarianLevel+1):
		if x == 2:
			settings.featuresAndTraits["Reckless Attack"] = "You can make your first attack reckless and gain advantage melee attacks using strength, however attack rolls against you have advantage as well."
			settings.featuresAndTraits["Danger Sense"] = "Advantage on Dexterity Saving Throws against effects you can see."
		if x == 3:
			#primal paths
			archetype = random.randint(0,1)
			if archetype == 0:
				settings.classArchetype = "Path of the Berserker"
			else:
				settings.classArchetype = "Path of the Totem Warrior"
			classArchetype(3,archetype)
			#totem warrior needs spells here(beast sense and speak with animal) as rituals
		if x == 4 or x == 8 or x == 12 or x == 16:#FIX!! this may have an issue where if both are the same it will only increment once
			randOne = random.randint(0,5)
			randTwo = random.randint(0,5)
			if randOne == 0 or randTwo == 0:
				settings.strength += 1
			if randOne == 1 or randTwo == 1:
				settings.dexterity += 1
			if randOne == 2 or randTwo == 2:
				settings.constitution += 1
			if randOne == 3 or randTwo == 3:
				settings.intelligence += 1
			if randOne == 4 or randTwo == 4:
				settings.wisdom += 1
			if randOne == 5 or randTwo == 5:
				settings.charisma += 1
		if x == 5:
			settings.featuresAndTraits["Extra Attack"] = "You can attack twice, instead of once, whenever you take the Attack action during your turn."
			settings.featuresAndTraits["Fast Movement"] = "Your speed increase by 10 feet while not wearing heavy armor."
			settings.speed += 10
		if x == 6:
			classArchetype(6,archetype)
		if x == 7:
			settings.featuresAndTraits["Feral Instrict"] = "You can advantage on initiative rolls. Additionally if you are surprised and not incapacitated you can act normally on your first turn if you rage."
		if x == 9:
			settings.featuresAndTraits["Brutal Critical"] = "You can roll one additional damage die for a critical hit. This increases to two dice at 13th level and three dice at 17th level."
		if x == 10:
			classArchetype(10,archetype)
		if x == 11:
			settings.featuresAndTraits["Relentless Rage"] = "If you drop to 0 hitpoints while raging you can make a DC 10 Con saving throw to retain 1 hitpoint. This DC increases by 5 each time used between rests."
		if x == 14:
			classArchetype(14,archetype)
		if x == 15:
			settings.featuresAndTraits["Persistent Rage"] = "Your rage will not end unless you end it or fall unconcious."
		if x == 18:
			settings.featuresAndTraits["Indomitable Might"] = "If your Strength check is less than your Strength score, you can use that instead."
		if x == 20:
			settings.featuresAndTraits["Primal Champion"] = "Your Strength and Constitution ability scores increase by 4."
			settings.strength += 4
			settings.constitution += 4

	proficiencyBonus(settings.level)

def classArchetype(classLevel, archetype):
	berserkerPath = {3:["Frenzy","When raging you can go into a Frenzy and make a single melee weapon attack as a bonus action on each turn after you go into the Frenzy.  When you end your rage you gain one exhaustion point"], 6:["Mindless Rage","While raging, you cannot be charmed or frightened."], 10:["Intimidating Presence","You can use your action to frighten someone within 30 feet of you. They must succeed a Wisdom saving throw (8 + Proficiency Bonus + Charisma Modifier) or become Frightened of you until the end of your next turn.  You can use susequent actions to continue this effect. This effect ends if they are more than 60 feet away from you."], 14:["Retaliation","When you take damage from a creature within 5 feet of you, you make use your reaction to make a melee attack on them."]}
	totemWarriorPath = {3:["Totem Spirit","Choose a totem spirit and gain its feature(PHB PG 50)"], 6:["Aspect of the Beast","Gain the magical benefits of a totem animal (PHB PG 50)"], 10:["Spirit Walker","Ritual casting of commune with nature and a totem spirit appears to convey the information you seek."], 14:["Totemic Attunement","Gain the magical benefits of a totem animal (PHB PG 50)"]}

	if archetype == 0:
		if classLevel == 3:
			settings.featuresAndTraits[berserkerPath[3][0]] = berserkerPath[3][1]
		if classLevel == 6:
			settings.featuresAndTraits[berserkerPath[6][0]] = berserkerPath[6][1]
		if classLevel == 10:
			settings.featuresAndTraits[berserkerPath[10][0]] = berserkerPath[10][1]
		if classLevel == 14:
			settings.featuresAndTraits[berserkerPath[14][0]] = berserkerPath[14][1]

	else:
		if classLevel == 3:
			settings.featuresAndTraits["Spirit Seeker"] = "You gain the ritual spells: Beast sense, Speak with Animals."
			settings.featuresAndTraits[totemWarriorPath[3][0]] = totemWarriorPath[3][1]
		if classLevel == 6:
			settings.featuresAndTraits[totemWarriorPath[6][0]] = totemWarriorPath[6][1]
		if classLevel == 10:
			settings.featuresAndTraits[totemWarriorPath[10][0]] = totemWarriorPath[10][1]
		if classLevel == 14:
			settings.featuresAndTraits[totemWarriorPath[14][0]] = totemWarriorPath[14][1]
	

