

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"
n = len(charset)

def f(a,b,n,x):
	return (a*x+b)%n

def f_inv(a,b,n,x):
	return ((x-b) * pow(a,-1,n)) % n 

def permute(message):
	p = [4, 3, 0, 5, 1, 2, 10, 9, 6, 11, 7, 8, 16, 15, 12, 17, 13, 14, 22, 21, 18, 23, 19, 20, 28, 27, 24, 29, 25, 26, 34, 33, 30, 35, 31, 32, 40, 39, 36, 41, 37, 38, 46, 45, 42, 47, 43, 44]
	permuted = [ message[p[i]] for i in range(len(message))]
	return ''.join(permuted)

def round(message,A,B,n):
	encrypted = ""
	for i in range(len(message)):
		x = charset.index(message[i])
		a = A[i%6]
		b = B[i%6]
		x = f(a,b,n,x)
		encrypted += charset[x]
	return permute(encrypted)

def encrypt(message):
	encrypted = message
	for k in range(6):
		A = [ rd.randint(2,n-1) for i in range(6)]
		B = [ rd.randint(1,n-1) for i in range(6)]
		encrypted = round(encrypted,A,B,n)
	return encrypted

p = [4, 3, 0, 5, 1, 2, 10, 9, 6, 11, 7, 8, 16, 15, 12, 17, 13, 14, 22, 21, 18, 23, 19, 20, 28, 27, 24, 29, 25, 26, 34, 33, 30, 35, 31, 32, 40, 39, 36, 41, 37, 38, 46, 45, 42, 47, 43, 44]

def decrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f_inv(a,b,n,x)
		encrypted += charset[x]

	return encrypted


cipher =  'C_ef8K8rT83JC8I0fOPiN6P!liE03W2NXFh1viJCROAqXb6o'
#A = 50 40 39 34 35 37
#B = 42 61 31 58 26 28

A = [50,40,39,34,35,37]
B = [42,61,31,58,26,28]

decipher = [0 for i in range(48)]


for i in range(6):
	for k in range(8):
		decipher[k*6+i] = decrypt(cipher,A[i],B[i],n)[k*6+i]


print("".join(decipher))