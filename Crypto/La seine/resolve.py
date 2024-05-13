from math import sqrt
from decimal import *
getcontext().prec = 1000


"""
a = Decimal(227701039519615111410834658518897187762295748074693093212569130723307389439403443666385689827602636587092673401419121005)
b = Decimal(-6577033815473856244766339529894200713834301217128629217207466250930633285308063864838059161008338809347850073081782432156817613643411619840)
c = Decimal(47492484265262348254625577324943989258788145447836992707268954207557944104098384493037232010048044182858300753126239188895399553237445100666825233679135745715)

delta = Decimal(b*b - 4*a*c)
print(delta)

delta = Decimal((delta).sqrt())
print(delta)

dessus = Decimal(-b + Decimal(delta))
dessus2 = Decimal(-b + Decimal(delta))
dessous = Decimal(Decimal(2)*a)

x1 = Decimal(dessus/dessous)
x2 = Decimal(-b - Decimal((delta)))/Decimal(Decimal(2)*a)


print(x1)

print("-----------------------------------------------------------------")

print(x2)



"""
possible = "abcdefghijklmnopqrstuvwxyz1023456789ABCDEFGHIJKLMNOPQRSTUVWXYZ{}()/_-"


def long_to_bytes(n):
    # Conversion de l'entier long en hexadécimal
    hex_string = "%x" % n
    # Vérification de la longueur de la chaîne hexadécimale
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string  # Ajout d'un zéro initial si nécessaire
    # Conversion hexadécimale en bytes
    byte_string = bytes.fromhex(hex_string)
    return byte_string


xf1 = Decimal(477173752345818692600581355718544587767356535417264155125042)
yf1 = Decimal(2499918363947345248591048685501369096723567302825670354829)
xf0 = Decimal(17758757388721541617454975427677274505216)
AB = Decimal(388070793197506567215490364778692980485)
a = Decimal(14372069526398118991)

for k in range(0,2**15):
    a2 = Decimal(a + k)
    if k % 100000 == 0:
    	print(k)
    b = Decimal((AB-a2*a2))
    b = Decimal(b.sqrt())
    #print("b : ", int(b))
    xf0 = Decimal((a2*xf1 + b*yf1)/AB)
    yf0 = Decimal((b*xf1 - a2*yf1)/AB)
    #print("xf0 : ", int(xf0))
    flag = long_to_bytes(int(xf0)).decode(errors="ignore")
    flag2 = long_to_bytes(int(yf0)).decode(errors="ignore")
    if all(char in possible for char in flag) and "404CTF{" in flag:
    	print(flag)
    	print(flag2)
    	print("a : ",a)
    	print("b : ",int(b))

