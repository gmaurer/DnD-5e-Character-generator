

def init():
	global race
	race = None
	global background
	background = None
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




