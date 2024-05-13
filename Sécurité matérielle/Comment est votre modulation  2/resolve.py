import numpy as np

NB_SUBCARRIERS = 8
F_C = 7e3
F_E = int(50*F_C)
R = 1000
T = 1/R


def QAM16(symbol):
    return -3+2*(symbol>>2)+1j*(3-2*(symbol&0b11))


data = np.fromfile('flag.iq', dtype='complex64')

def integral(func,k):
    somme = 0
    for i in range(len(func)):
        somme += (func[i]*np.exp(-2j*np.pi*k*(i/350)))
    return (somme/350)



def QAM16_demod(symbol):
    re = np.real(symbol)
    im = np.imag(symbol)
    re_part = (re + 3) / 2
    im_part = (3 - im) / 2
    return (int(re_part) << 2) + int(im_part)




QAM16_demod = {(-3,+3) : 0,
(-3,+1) : 1,
(-3,-1) : 2,
(-3,-3) : 3,
(-1,+3) : 4,
(-1,+1) : 5,
(-1,-1) : 6,
(-1,-3) : 7,
(1,+3) : 8,
(1,+1) : 9,
(1,-1) : 10,
(1,-3) : 11,
(3,+3) : 12,
(3,+1) : 13,
(3,-1) : 14,
(3,-3) : 15}



flag = b""

for i in range(len(data)//350):
    for k in range(4):
        octet = 0
        res = integral(data[(i)*350:(i+1)*350],2*k)
        res = (round(res.real),round(res.imag))
        res = QAM16_demod[res]
        octet += res << 4
        res = integral(data[(i)*350:(i+1)*350],2*k+1)
        res = (round(res.real),round(res.imag))
        res = QAM16_demod[res]

        octet += res

        flag += bytes([octet])



print(flag)

with open('flag.png','wb') as f:
    f.write(flag)