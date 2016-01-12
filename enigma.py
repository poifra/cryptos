import random
from collections import deque

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Rotor:
	def __init__(self,transitions = None):
		if transitions is None:
			self.transitions = deque(list(ALPHABET))
			while self.transitions[0] is 'a':
				self.transitions.rotate(random.randint(1,25))
		else:
			self.transitions = transitions
		self.position = 0
	def correspondance(self,letter):
		return self.transitions[ALPHABET.index(letter)]
	def shift(self):
		self.transitions.rotate(1)

class EnigmaKey:
	def __init__(self):
		self.rotor1 = Rotor()
		self.rotor2 = Rotor()
		self.rotor3 = Rotor()
	def encrypt(self,letter):
		self.rotor1.shift()
		self.rotor1.position += 1
		if self.rotor1.position == 26:
			self.rotor1.position = 0
			self.rotor2.shift()
			self.rotor2.position += 1
			if self.rotor2.position == 26:
				self.rotor2.position = 0
				self.rotor3.shift()
				self.rotor