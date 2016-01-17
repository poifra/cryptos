import random
from collections import deque
from copy import deepcopy

ALPHABET = "abcdefghijklmnopqrstuvwxyz "
SIZE = len(ALPHABET)

def cesar(n, message, mode):
	'''
	cesar cipher
	'''
	res = ''
	if mode == 'enc':
		for c in message:
			res += ALPHABET[(find(c) + n) % SIZE]
	elif mode == 'dec':
		for c in message:
			res += ALPHABET[(find(c) - n) % SIZE]
	else:
		raise ValueError("use 'enc' or 'dec' (without quotes) as mode")

def vigenere(key, message, mode):
	'''
	Vigenere cipher
	'''
	pad = ''
	res = ''
	while len(pad) < len(message):
		pad += key

	if mode == 'enc':
		for i in range(len(message)):
			newPos = (ALPHABET.find(message[i]) + ALPHABET.find(pad[i])) % SIZE
			res += ALPHABET[newPos]
	elif mode == 'dec':
		for i in range(len(message)):
			newPos = (ALPHABET.find(message[i]) - ALPHABET.find(pad[i])) % SIZE
			res += ALPHABET[newPos]
	else:
		raise ValueError("use 'enc' or 'dec' (without quotes) as mode")

	return res

class Rotor:
	def __init__(self, reflector = False, transitions = None):
		self.nbDecal = 0
		self.reflector = reflector
		if transitions is None:
			self.transitions = deque(list(ALPHABET))
			while self.transitions[0] is 'a':
				self.transitions.rotate(random.randint(1,25))
		else:
			self.transitions = transitions
		self.originalTransition = deepcopy(self.transitions)
		self.startPos = self.transitions[0]
		self.position = 0

	def correspondance(self,letter):
		return self.transitions[ALPHABET.index(letter)]

	def shift(self):
		self.nbDecal += 1
		self.transitions.rotate(1)

	def toString(self):
		return "original : "+str(self.originalTransition)+" current : "+str(self.transitions)

	def reset(self):
		self.transitions = self.originalTransition
		self.nbDecal = 0
		
class EnigmaKey:
	def __init__(self, letterFlips = None):
		self.rotor1 = Rotor()
		self.rotor2 = Rotor()
		self.rotor3 = Rotor()
		self.reflector = Rotor(reflector = True)
		if letterFlips is None:
			self.letterFlips = dict()
			for letter in ALPHABET:
				self.letterFlips[letter] = letter
		else:
			self.letterFlips = letterFlips
	def encrypt(self,letter):
		self.rotor1.shift()
		if self.rotor1.nbDecal == 26:
			self.rotor2.shift()
			self.rotor1.nbDecal = 0
			if self.rotor2.nbDecal == 26:
				self.rotor3.shift()
				self.rotor2.nbDecal = 0
		transition = self.rotor1.correspondance(letter)
		transition = self.rotor2.correspondance(transition)
		transition = self.rotor3.correspondance(transition)
		transition = self.reflector.correspondance(transition)
		transition = self.rotor3.correspondance(transition)
		transition = self.rotor2.correspondance(transition)
		transition = self.rotor1.correspondance(transition)
		return transition
	
	def reset(self):
		self.rotor1.reset()
		self.rotor2.reset()
		self.rotor3.reset()

	def getKey(self):
		return "Start positions : "+self.rotor1.startPos+", "+self.rotor2.startPos+", "+self.rotor3.startPos
		
	def toString(self):
		print(self.rotor1.toString())
		print(self.rotor2.toString())
		print(self.rotor3.toString())
		
class RSAKey:
	pass
