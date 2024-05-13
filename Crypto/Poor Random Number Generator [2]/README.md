
# Poor random number generator 2/2

La vulnerabilite dans le generateur de viens de cette ligne :
```
combine = lambda x1,x2,x3 : (x1 and x2)^(x1 and x3)^(x2 and x3)
```

Si x1 vaut 1, alors combine(x1,x2,x3) a 75 % de chances de valoir 1 ; et si x1 vaut 0, alors combine(x1,x2,x3) a 75 % de chances de valoir 0. Il en va de même pour x2 et x3. Sachant cela, on peut tester toutes les graines différentes pour le premier LFSR et voir laquelle est corrélée à 75 % avec les octets utilisés pour XORer le flag (que l'on peut obtenir car on connaît une partie du flag en clair). En faisant cela pour les trois LFSR, on peut retrouver l'état initial du générateur et trouver le flag.

