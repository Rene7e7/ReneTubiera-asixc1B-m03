"""
Rene Tubiera
Exercici 18
Escriu un programa que donat el nom i els dos cognoms introduïts
per un usuari, mostri, només, les inicials corresponents en majúscules.

"""

nom = input("Dime tu nombre: ")
cognom1 = input("Dime tu apellido: ")
cognom2 = input("Dime tu apellido: ")
print(nom[0].upper() + cognom1[0].upper() + cognom2[0].upper())

"""
nom = input("Dime tu nombre: ")
cognom1 = input("Dime tu primer apellido: ")
cognom2 = input("Dime tu segundo apellido: ")
print(nom.capitalize()+ " " + cognom1.capitalize() + " " + cognom2.capitalize())
"""
