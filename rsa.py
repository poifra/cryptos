from random import SystemRandom
from collections import deque
from copy import deepcopy
from cryptos import ALPHABET as ALPHABET
from cryptos import SIZE as SIZE

TEST_PRECISION = 64
cryptoGen = SystemRandom()

class RSAKey:
	def __init__(self, p=-1,q=-1, keysize=2048):
		self.keysize = keysize
		if(p == -1 or q == -1):
			self.p = self._getPrime()
			self.q = self._getPrime()
		else:
			self.p = p
			self.q = q

def _getPrime(keysize=2048):
	ks = keysize
	while True:
		prime = cryptoGen.randint(2**(ks-1),2**(ks+1))
		prime |= 1 #make sure it's odd
		if(len(bin(prime))-2 == ks and _isPrime(prime,TEST_PRECISION)):
			return prime

def _isPrime(n,nbTrials):
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


def _gcd(self,a,b):
	while b != 0:
		if a < b:
			(a,b) = (b,a%b)
	return a

