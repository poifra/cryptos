import random
from collections import deque
from copy import deepcopy

ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()
SIZE = len(ALPHABET)

def cesar(n, message, mode):
	'''
	cesar cipher
	'''
	res = ''
	if mode == 'enc':
		for c in message:
			res += ALPHABET[(ALPHABET.find(c) + n) % SIZE]
	elif mode == 'dec':
		for c in message:
			res += ALPHABET[(ALPHABET.find(c) - n) % SIZE]
	else:
		raise ValueError("use 'enc' or 'dec' (without quotes) as mode")

	return res

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
			self.transTable = deque()
			cpyAlpha = list(deepcopy(ALPHABET))
			random.shuffle(cpyAlpha)
			for c in ALPHABET:
				self.transTable.append(cpyAlpha.pop())
			
		else:
			if type(transitions) is str:
				self.transTable = deque(transitions)
			else:
				self.transTable = transitions
		self.originalTransition = deepcopy(self.transTable)
		self.startPos = self.transTable[0]
		self.position = 0

	def correspondance(self,letter):
		return self.transTable[ALPHABET.index(letter)]

	def shift(self):
		self.nbDecal += 1
		self.transTable.rotate(1)

	def toString(self):
		subs = ''
		for c in self.transTable:
			subs += c
		return subs

	def reset(self):
		self.transTable = self.originalTransition
		self.nbDecal = 0
		
class EnigmaKey:
	def __init__(self, letterFlips = None):
		self.leftRotor = Rotor(transitions = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ')
		self.midRotor = Rotor(transitions = 'AJDKSIRUXBLHWTMCQGZNPYFVOE')
		self.rightRotor = Rotor(transitions = 'BDFHJLCPRTXVZNYEIWGAKMUSQO')
		self.reflector = Rotor(reflector = True, transitions = "YRUHQSLDPXNGOKMIEBFZCWVJAT")
		if letterFlips is None:
			self.letterFlips = dict()
			for letter in ALPHABET:
				self.letterFlips[letter] = letter
		else:
			self.letterFlips = letterFlips
	def encrypt(self,letter):
		'''
		Enigma Process
		1. Validate input
		2. Rotate wheels
		3. Pass through plugboard
		4. Pass through right-hand wheel
		5. Pass through middle wheel
		6. Pass through left-hand wheel
		7. Pass through reflector
		8. Pass through left-hand wheel
		9. Pass through middle wheel
		10. Pass through right-hand wheel
		11. Pass through plugboard
		12. Convert to output letter
		'''
		self._rotateRotors()
		print("init letter " + letter)
		transition = self.leftRotor.correspondance(letter)
		print("it became " + transition + " after left rotor")
		transition = self.midRotor.correspondance(transition)
		print("it became " + transition + " after mid rotor")
		transition = self.rightRotor.correspondance(transition)
		print("it became " + transition + " after right rotor")
		transition = self.reflector.correspondance(transition)
		print("it became " + transition + " after reflector")
		transition = self.rightRotor.correspondance(transition)
		print("it became " + transition + " after right rotor")
		transition = self.midRotor.correspondance(transition)
		print("it became " + transition + " after mid rotor")
		transition = self.leftRotor.correspondance(transition)
		print("it became " + transition + " after left rotor")

		return transition
	
	def _rotateRotors(self):
		self.leftRotor.shift()
		if self.leftRotor.nbDecal == 26:
			self.midRotor.shift()
			self.leftRotor.nbDecal = 0
			if self.midRotor. shift == 26:
				self.rightRotor.shift()
				self.midRotor.nbDecal = 0
	
	def reset(self):
		self.leftRotor.reset()
		self.midRotor.reset()
		self.rightRotor.reset()

	def getKey(self):
		return "Start positions : "+self.leftRotor.startPos+", "+self.midRotor.startPos+", "+self.leftRotor.startPos
		
	def toString(self):
		print(ALPHABET)
		print(self.leftRotor.toString() + " left")
		print(self.midRotor.toString() + " mid")
		print(self.rightRotor.toString() + " right")
		print(self.reflector.toString() + " reflector")
		
class RSAKey:
	pass
