

def init():
	global race
	race = None
	global background
	background = None
	global classes
	classes = None
	#base level and class level
	global level
	level = 0
	global barbarianLevel
	barbarianLevel = 0
	global clericLevel
	clericLevel = 0
	global druidLevel
	druidLevel = 0
	global fighterLevel
	fighterLevel = 0
	global monkLevel
	monkLevel = 0
	global paladinLevel
	paladinLevel = 0
	global rangerLevel
	rangerLevel = 0
	global rogueLevel
	rogueLevel = 0
	global sorcererLevel
	sorcererLevel = 0
	global warlockLevel
	warlockLevel = 0
	global wizardLevel
	wizardLevel = 0
	#stats
	global strength
	global dexterity
	global constitution
	global intelligence
	global wisdom
	global charisma
	strength = 0
	dexterity = 0
	constitution = 0
	intelligence = 0
	wisdom = 0
	charisma = 0
	global abilityScoreModifier
	abilityScoreModifier = {1:-5,2:-4,3:-4,4:-3,5:-3,6:-2,7:-2,8:-1,9:-1,10:0,11:0,12:1,13:1,14:2,15:2,16:3,17:3,18:4,19:4,20:5,21:5,22:6,23:6,24:7,25:7,26:8,27:8,28:9,29:9,30:10}
	#hp
	global hitPoints
	hitPoints = 0
	#speed
	global speed
	speed = 0
	#proficencies
	global proficiencies
	proficiencies = []
	#age
	global age
	age = 0
	#alignment
	global alignment
	alignment = None
	#size(feet)	
	global size
	size = 0.0
	#weight(pounds)
	global weight
	weight = 0.0
	#features and traits
	global featuresAndTraits 
	featuresAndTraits = {}
	#what tools you are proficient in
	global toolProficiencies
	toolProficiencies = []
	#languages known
	global languages
	languages = []
	#all skills 
	global skills
	skills = {"Athletics":0, "Acrobatics":0, "Sleight of Hand":0, "Stealth":0, "Arcana":0, "History":0, "Investigation":0, "Nature":0, "Religion":0, "Animal Handling":0, "Insight":0, "Medicine":0, "Perception":0, "Survival":0, "Deception":0, "Intimidation":0, "Performance":0, "Persuasion":0}
	#feats
	global feats
	feats = {}
	#items make into dic so you can have quantity?
	global equipment
	equipment = {}
	#wealth in gp, sp, cp
	global wealth
	wealth = {"Gold":0,"Silver":0,"Copper":0}
	global hitDice
	hitDice = 0
	global savingThrow
	savingThrow = {"Dexterity":0, "Strength":0, "Constitution":0, "Intelligence":0, "Wisdom":0, "Charisma":0}
	global proficiencyBonus
	proficiencyBonus = 0
	global ragesToLevel
	ragesToLevel = {1:[2,2], 2:[2,2], 3:[3,2], 4:[3,2], 5:[3,2], 6:[4,2], 7:[4,2], 8:[4,2], 9:[4,3], 10:[4,3], 11:[4,3], 12:[5,3], 13:[5,3], 14:[5,3], 15:[5,3], 16:[5,4], 17:[6,4], 18:[6,4], 19:[6,4],20:[99,4]}
	global rages
	rages = None
	global rageBonus
	rageBonus = None



