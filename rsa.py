from random import SystemRandom
from collections import deque
from copy import deepcopy
from oldschool import ALPHABET as ALPHABET
from oldschool import SIZE as SIZE

TEST_PRECISION = 512
cryptoGen = SystemRandom()

def getPrime(keysize=1024):
	ks = keysize
	while True:
		prime = cryptoGen.randint(2**(ks-1),2**(ks+1))
		prime |= 1 #make sure it's odd
		if(len(bin(prime))-2 == ks and _isProbablePrime(prime,TEST_PRECISION)):
			return prime

def isProbablePrime(n,nbTrials):
	s = 0
	d = n-1
	while True:
		quotient, remainder = divmod(d,2)
		if remainder == 1:
			break
		s += 1
		d = quotient

	assert 2**s * d == n-1

	def millerWitness(a):
		x = pow(a,d,n)
		if x == 1:
			return False
		for i in range(s):
			x = pow(a,2**i * d,n)
			if x == n-1:
				return False
		return True

	for i in range(nbTrials):
		witness = cryptoGen.randint(2,n-1) #randint returns a number in [a,b[
		if(millerWitness(witness)):
			return False
	return True


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
	print(getPrime())