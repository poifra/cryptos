import random

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Rotor
	def __init__(self,transitions = None):
		if transitions is None:
			self.transitions = dict()
			for c in ALPHABET:
				sub = random.choice(c)

				while sub is c:
					sub = random.choice(c)

				transitions[c] = sub
		else:
			self.transitions = transitions

	def getNextTransition(self):
		pass

class EnigmaKey:
	def __init__(self):
			self.rotor1 = Rotor()
			self.rotor2 = Rotor()
			self.rotor3 = Rotor()
	def encrypt(self,letter):
		pass