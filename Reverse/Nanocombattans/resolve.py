import subprocess

for i in range(256):
	with open("payload" + str(i), "w") as file:
	    file.write('fi3r_n4n0comb4tt' + chr(i)*0x3)

