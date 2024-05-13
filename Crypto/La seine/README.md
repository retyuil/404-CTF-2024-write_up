
# La seine

Ce challenge de cryptographie est le plus difficile que j'ai réussi à faire.

En étudiant le système de signature fourni, on se rend compte que pour tout n, x2n = (a*a + b*b) * x_2n+2

Ainsi, pour la deuxième signature, on sait que x_0 = (a*a+b*b)^(k//2) * x_2k sachant que l'on connaît x_0 et x_2K  (c'est-à-dire la première partie de la signature).  On peut alors calculer la racine k//2 ieme de (x0)*(x_2k)^-1 on peut donc retrouver (a*a+*b*b).

LLa première signature est un peu plus complexe. En effet, on sait seulement que :

x_1 = ((a*a+b*b)^(k//2) * x_2k+1) avec un k inconnu, on peut le retrouver car x_1 va etre beaucoup plus petit que tous les autres x car x_1 est tres petit devant p.

On peut donc retrouver x_1.

Or on sait que x_1 = x_0*a + y_0 * b et y_1 = x_0*b - y_0*a

En combinant ces deux équations, on peut exprimer a en fonction  de x_1,y_1,x_0 et de (a*a+*b*b) sous la forme d'une équation du second degré. On connaît toutes ces variables sauf x_0 mais on sait que le flag commence par "404CTF{", donc on connaît les 48 bits de poids fort de x_0 on peut donc trouver une valeur tres proche de x_0 et donc de a.

Maintenant que l'on connaît une valeur proche de a, on peut juste tester toutes les valeurs proches du a obtenu et calculer et espérer trouver une première partie du flag composée de caractères alphanumériques.

Dans le fichier resolve.py, vous trouverez la résolution de l'équation du second degré et le test des différents flags.

Et dans le notebook SageMath, vous trouverez le reste des calculs.