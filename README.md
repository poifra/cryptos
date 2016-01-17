# cryptos
Implementation of various cryptographic ciphers done in Python 3.x. No external dependencies. This is mostly for fun and all random sources use Python's built-in random module, so use at your own risk.

In the future, this module will also probably contain statistical tools to help with breaking codes.

Current available ciphers are :

### Cesar cipher 
https://en.wikipedia.org/wiki/Caesar_cipher

The most simple cipher you can have. It is a simple mono-alphabetic substitution. To use it, call cryptos.cesar(n, message, mode) where n is the shift you want to make and mode is either 'enc' for encryption or 'dec' for decryption (without quotes). Note that for n = 13, this is a ROT13 encryption and therefore, encryption and decryption will yield the same results.

### Vigenere cipher
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

The well-known poly-alphabetic cipher. It's usage is similar to Cesar's. Call cryptos.vigenere(key, message, mode) where mode is either 'enc' or 'dec'.

### Enigma (buggy)
https://en.wikipedia.org/wiki/Enigma_machine

Simulation of the German machine used during WW2. This is a 3-rotor machine, with a reflector. The rotor subsitutions are randomly generated, but I plan to add customisable rotors, for more historically-accurate fun. Many features are still missing, like swapping rotors around and maybe a customisable amount of rotors. 

Currently, you can't decrypt. So it's very secure :P

### Future plans
+ Finish Enigma
  + Steckers
  + Customisable rotors
+ RSA
+ DES
+ AES
