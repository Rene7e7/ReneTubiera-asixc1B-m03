"""
Rene Tubiera Sadinas
19/10/23
M03
UF1
Pp1B Prova Practica
ASIXc1B
Exercici: calcula la diagonal d'un rectangle
"""
# Fem un import math per fer el sqrt()
import math

# Demanem a l'usuari que doni un valor a l'alçada i amplada
alcada = int(input("Donem un valor per el alçada"))
amplada = int(input("Donem un valor per el amplada"))

# Es el calcul del diagonal de un rectangle
diagonal = math.sqrt(alcada**2+amplada**2)

# Mostra per pantalla el resultat del cálcul utilitzant el variable diagonal
print("El resultat del calcul del diagonal del rectangle es: ", diagonal)
