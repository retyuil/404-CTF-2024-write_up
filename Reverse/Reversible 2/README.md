
# Revers(ibl)e Engineering [2/2]

Ce challenge ressemble beaucoup au précédent, à la différence que la cible change à chaque lancement du binaire et à chaque étape. La fonction qui chiffre la clé reste la même tout au long, mais elle n'est pas contenue dans le binaire ; elle est obtenue en faisant une requête à un serveur qui ne peut être effectuée qu'une seule fois.

Nous pouvons récupérer la cible modifiée en observant quelle chaîne est comparée à notre entrée modifiée. Cependant, pour extraire la fonction qui modifie notre entrée, j'ai décidé d'utiliser un script GDB :


```
set logging file a.txt
set logging on

br *0x55555555531f
br *0x55555555533f

run
checkpoint
c

s
n 10 
checkpoint
n
x/2x 0x7fffffffdc50


restart 2
set {unsigned char[8]}0x7fffffffdc50 = {0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7}
checkpoint
n 
x/2x 0x7fffffffdc50 

restart 3
set {unsigned char[8]}0x7fffffffdc50 = {0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf}
checkpoint
n 
x/2x 0x7fffffffdc50 

...

restart 32
set {unsigned char[8]}0x7fffffffdc50 = {0xf0, 0xf1, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6, 0xf7}
checkpoint
n 
x/2x 0x7fffffffdc50 

restart 33
set {unsigned char[8]}0x7fffffffdc50 = {0xf8, 0xf9, 0xfa, 0xfb, 0xfc, 0xfd, 0xfe, 0xff}
checkpoint
n 
x/2x 0x7fffffffdc50 

```

Je modifie les registres qui contiennent l'entrée de la fonction et je récupère la sortie pour chaque octet différent possible. Avec cela, je peux savoir comment mon entrée va être transformée et je peux trouver quelle entrée choisir pour qu'elle soit égale à la cible.
