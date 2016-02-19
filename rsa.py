from random import SystemRandom
from collections import deque
from copy import deepcopy

TEST_PRECISION = 256
cryptoGen = SystemRandom()

def getPrime(keysize=1024):
	ks = keysize
	while True:
		prime = cryptoGen.randint(2**(ks-1),2**(ks+1))
		prime |= 1 #make sure it's odd
		if(len(bin(prime))-2 == ks and isProbablePrime(prime)):
			return prime

def rabinMiller(num):
	# Returns True if num is a prime number.
	import random
	s = num - 1
	t = 0
	while s % 2 == 0:
		# keep halving s while it is even (and use t
		# to count how many times we halve s)
		s = s // 2
		t += 1

	for trials in range(TEST_PRECISION):
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1: # this test does not apply if v is 1.
			i = 0
			while v != (num - 1):
				if i == t - 1:
					return False
				else:
					i = i + 1
					v = (v ** 2) % num
	return True


def isProbablePrime(n):

	lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
	101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
	211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 
	337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 
	461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 
	601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
	739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 
	881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

	if n in lowPrimes : return True

	for p in lowPrimes:
		if n % p == 0 : return False

	return rabinMiller(n)


def egcd(a,b):
	'''
	Returns a triplet g,x,y such that ax+by == g == gcd(a,b)
	'''
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q,r = b//a, b%a
		m,n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd,x,y

def modinv(a,b):
	gcd,x,y = egcd(a,b)
	if gcd != 1:
		return None
	else:
		return x % b

class RSAKey:
	def __init__(self, p=-1,q=-1, keysize=2048):
		self.keysize = keysize
		if(p == -1 or q == -1):
			self.p = getPrime(self.keysize//2)
			self.q = getPrime(self.keysize//2)
		else:
			self.p = p
			self.q = q
		self.n = self.p * self.q
		self.phi = (self.p-1) * (self.q-1)
		self.d = cryptoGen.randint(1,self.phi+1)
		while egcd(self.phi,self.d)[0] != 1:
			self.d = cryptoGen.randint(1,self.phi+1)
		self.e = modinv(self.d,self.phi)
	def encrypt(self, m):
		return pow(m,self.e,self.n)
	def decrypt(self, c):
		return pow(c,self.d,self.n)

if __name__=='__main__':
	rsa = RSAKey()
	print("p =",rsa.p)
	print("q =",rsa.q)
	print("n =",rsa.n)	
	print("phi =",rsa.phi)
	print("e =",rsa.e)
	print("d =",rsa.d)
	valid = rsa.decrypt(rsa.encrypt(253)) == 253
	print("Validation : ((253^e)^d) mod n == 253", valid)
