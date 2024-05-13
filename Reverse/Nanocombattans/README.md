
# Nanocombattant

D'accord, voici le texte corrigé :

Ce challenge est de type nanomites, ce qui signifie que le programme étudié va démarrer un ou plusieurs sous-processus et interagir avec ces différents sous-processus en modifiant ou en récupérant les valeurs contenues dans leurs registres.

Ce type de binaire est très compliqué à analyser de manière dynamique. Heureusement pour nous, le programme possède une faille. En effet, quand le programme traite notre entrée, il examine chaque lettre une par une, et dès qu'il rencontre une lettre qui n'est pas la bonne, il s'arrête. Nous pouvons donc compter le nombre de fois où nous pouvons tester chaque lettre et voir laquelle va provoquer le plus d'appels à la fonction Ptrace.


