# Revers(ibl)e Engineering [0/2]

Dans ce challenge, on nous donne un circuit réversible composé uniquement de portes Toffoli, NOT et CNOT. On pourrait implémenter l'algorithme décrit ici : https://www.researchgate.net/publication/234791226_Data_structures_and_algorithms_for_simplifying_reversible_circuits, mais cela nous demanderait un peu de réflexion. Pourquoi faire cela quand on peut simplement bruteforcer tous les circuits possibles et trouver celui qui a le même effet que le circuit étudié (c'est-à-dire la même table de vérité) ?

Les circuits que l'on cherche à simplifier ont environ 8 portes, et il y a seulement 12^k circuits possibles avec k portes. On peut espérer pouvoir trouver un circuit équivalent en moins de 60 secondes avec Python on y arrive en moins de 2 secondes.