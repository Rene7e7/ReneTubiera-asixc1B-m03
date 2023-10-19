"""
Rene Tubiera Sadinas
19/10/23
M03
UF1
Pp1B Prova Practica
Exercici: calcula la diagonal d'un rectangle
"""
# Fem un import math per fer el sqrt()
import math

# Demanem a l'usuari que doni un valor a l'alçada i amplada
lenght = int(input("Donem un valor per el alçada"))
width = int(input("Donem un valor per el amplada"))

# Es el calcul del diagonal de un rectangle
diagonal = math.sqrt(lenght**2+width**2)

# Mostra per pantalla el resultat del cálcul utilitzant el variable diagonal
print("El resultat del calcul del diagonal del rectangle es: ", diagonal)
