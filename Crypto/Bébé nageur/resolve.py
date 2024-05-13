
import random as rd

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"


def f(a,b,n,x):
	return (a*x+b)%n

def f_inv(a,b,n,x):
	return ((x-b) * pow(a,-1,n)) % n 

def encrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f(a,b,n,x)
		encrypted += charset[x]

	return encrypted


def decrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f_inv(a,b,n,x)
		encrypted += charset[x]

	return encrypted


n = len(charset)
a = rd.randint(2,n-1)
b = rd.randint(1,n-1)


for a in range(2,n-1):
	for b in range(1,n-1):
		decrypted = decrypt('-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_',a,b,n)
		if '404' in decrypted:
			print(decrypted)


# ENCRYPTED FLAG : -4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_