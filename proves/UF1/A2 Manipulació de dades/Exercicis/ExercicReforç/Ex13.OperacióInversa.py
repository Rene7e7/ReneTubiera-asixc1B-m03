"""
Rene Tubiera Sadinas
Exercici 13
Escriu un programa que llegeixi un nombre i tot seguit calculi i mostri l'arrel quadrada i cúbica d'aquest número.
Desafortunadament, Python3 no té cap funció predefinida que calculi l'arrel cúbica, però sí que pots utilitzar l’operador que “fa l’operació inversa” …
"""

# Llegeix un nombre de l'usuari
nombre = float(input("Introdueix un nombre: "))

# Calcula l'arrel quadrada i cúbica
arrel_quadrada = nombre ** 0.5
arrel_cubica = nombre ** (1/3)

# Mostra els resultats
print(f"Arrel quadrada de {nombre} és: {arrel_quadrada}")
print(f"Arrel cúbica de {nombre} és: {arrel_cubica}")

