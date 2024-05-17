
# Revers(ibl)e Engineering [1/2]

Dans ce challenge, un serveur nous fournit un binaire différent à chaque fois.

En analysant le binaire, nous découvrons que notre entrée (un nombre hexadécimal de longueur 32, c'est-à-dire 16 octets) sera l'input d'une fonction effectuant plusieurs opérations et comparant le résultat avec une chaîne de caractères hexadécimaux contenue dans le binaire. Voici un extrait de la fonction :

```
 1275:   88 45 ef                mov    %al,-0x11(%rbp)
    1278:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    127c:   c1 f8 04                sar    $0x4,%eax
    127f:   83 e0 01                and    $0x1,%eax
    1282:   89 c2                   mov    %eax,%edx
    1284:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    1288:   c1 f8 05                sar    $0x5,%eax
    128b:   21 c2                   and    %eax,%edx
    128d:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    1291:   31 d0                   xor    %edx,%eax
    1293:   88 45 ef                mov    %al,-0x11(%rbp)
    1296:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    129a:   c1 f8 06                sar    $0x6,%eax
    129d:   83 e0 01                and    $0x1,%eax
    12a0:   89 c2                   mov    %eax,%edx
    12a2:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12a6:   21 d0                   and    %edx,%eax
    12a8:   c1 e0 02                shl    $0x2,%eax
    12ab:   89 c2                   mov    %eax,%edx
    12ad:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12b1:   31 d0                   xor    %edx,%eax
    12b3:   88 45 ef                mov    %al,-0x11(%rbp)
    12b6:   80 75 ef 10             xorb   $0x10,-0x11(%rbp)
    12ba:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12be:   c0 e8 07                shr    $0x7,%al
    12c1:   0f b6 c0                movzbl %al,%eax
    12c4:   0f b6 55 ef             movzbl -0x11(%rbp),%edx
    12c8:   c1 fa 04                sar    $0x4,%edx
    12cb:   83 e2 01                and    $0x1,%edx
    12ce:   21 d0                   and    %edx,%eax
    12d0:   01 c0                   add    %eax,%eax
    12d2:   89 c2                   mov    %eax,%edx
    12d4:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12d8:   31 d0                   xor    %edx,%eax
    12da:   88 45 ef                mov    %al,-0x11(%rbp)
    12dd:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12e1:   c0 e8 04                shr    $0x4,%al
    12e4:   0f b6 c0                movzbl %al,%eax
    12e7:   c1 e0 05                shl    $0x5,%eax
    12ea:   83 e0 20                and    $0x20,%eax
    12ed:   89 c2                   mov    %eax,%edx
    12ef:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12f3:   31 d0                   xor    %edx,%eax
    12f5:   88 45 ef                mov    %al,-0x11(%rbp)
    12f8:   0f b6 45 ef             movzbl -0x11(%rbp),%eax
    12fc:   d0 e8                   shr    $1,%al
    12fe:   0f b6 c0                movzbl %al,%eax
```

Le défi est que nous n'avons que 20 secondes pour trouver la bonne entrée, et que la fonction et la cible changent à chaque fois.

J'ai donc décidé de créer un programme Python qui convertit le code assembleur ci-dessous en code Python, ce qui nous permettra de brute force  chaque octet avec Python et finalement de trouver la bonne entrée. Pour extraire le code assembleur et la cible, j'utilise objdump sur Debian.






