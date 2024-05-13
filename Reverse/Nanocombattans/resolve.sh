#!/bin/bash

# Boucle pour exécuter la commande pour chaque payload
for ((i=0; i<256; i++))
do
    # Exécute la commande avec strace et stocke la sortie dans un fichier différent pour chaque payload
    strace ./nanocombattant < "payload$i" > "output_$i.txt" 2>&1
done
