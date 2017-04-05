import settings
import random

def alignmentPick(lawNeuCha,gooNeuEvi):

	mutant = random.uniform(0,1)
	if mutant < 0.15:
		lawNeuCha = ["Lawful", "Neutral", "Chaotic"]
		gooNeuEvi = ["Good", "Neutral", "Evil"]

	first = random.choice(lawNeuCha)
	second = random.choice(gooNeuEvi)
	settings.alignment = " ".join((first,second))

