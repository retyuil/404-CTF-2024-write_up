from pwn import xor
from LFSR import LFSR
from generator import CombinerGenerator
import random as rd
with open('flag.png.part','rb') as f:
	known = f.read()


with open('flag.png.enc','rb') as f:
	cipher = f.read()[:len(known)]

key = (xor(cipher,known))

poly1 = [19,5,2,1] # x^19+x^5+x^2+x
poly2 = [19,6,2,1] # x^19+x^6+x^2+x
poly3 = [19,9,8,5] # x^19+x^9+x^8+x^5

print(key)


'''

def correlation(key1,key2):
	somme = 0
	for i in range(280):
		if key1[i] == key2[i]:
			somme += 1
	return somme


key_bin = ''
print(key.hex())
for byte in key:
	key_bin += str(bin(byte)[2:].zfill(8))

maximum = 0
for i in range(2**19):
	if i % 2048 == 0:
		print(i)
	key_gen = ''
	state = bin(i)[2:].zfill(19)
	state = list(state)
	for k in range(19):
		state[k] = int(state[k])
	LFSR1 = LFSR(poly3,state)
	for i in range(280):
		key_gen += str(LFSR1.generateBit())
	corre = correlation(key_gen,key_bin)
	if corre >= maximum:
		maximum = corre
		best_state = state
	

print(maximum)
print(best_state)
'''
state1 = [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
state2 = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
state3 = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1]


combine = lambda x1,x2,x3 : (x1 and x2)^(x1 and x3)^(x2 and x3)

#Create LFSRs
L1 = LFSR(fpoly=poly1,state=state1)
L2 = LFSR(fpoly=poly2,state=state2)
L3 = LFSR(fpoly=poly3,state=state3)

#Create (secure) generator
generator = CombinerGenerator(combine,L1,L2,L3)

key = b''
for i in range(40154):
	key += (generator.generateByte())

with open('flag.png.enc','rb') as f:
	cipher = f.read()

decode = xor(cipher,key)

with open('flag.png','wb') as f:
	cipher = f.write(decode)