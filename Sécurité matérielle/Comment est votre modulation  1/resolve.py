import struct
import matplotlib.pyplot as plt

with open('flag.raw','rb') as f:
	data = f.read()


f = []
for i in range(len(data)//4):
	f.append(struct.unpack('f', data[i*4:(i+1)*4])[0])

time = [i for i in range(len(f))]

plt.plot(time,f)
plt.show()
maxi = []

for k in range(len(f)//350):
	res = max(f[k*350:(k+1)*350])*255
	res = int(res)
	res = bytes([res])
	maxi.append(res)


im = b''
for i in maxi:
	im += i

with open('flag.png','wb') as f:
	f.write(im)
