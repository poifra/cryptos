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