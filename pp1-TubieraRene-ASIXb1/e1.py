"""
Rene Tubiera Sadinas
19/10/23
M03
UF1
Calcul diagonal
"""
import math
# Demanem a l'usuari que doni un valor a l'alçada i amplada
lenght = int(input("Donem un valor per el alçada"))
width = int(input("Donem un valor per el amplada"))

# Es el calcul del diagonal de un rectangle
diagonal = math.sqrt(lenght**2+width**2)

# Mostra per pantalla le resulta del calcul utilitzant el variable diagonal
print("El resultat del calcul del diagonal del rectangle es: ", diagonal)
