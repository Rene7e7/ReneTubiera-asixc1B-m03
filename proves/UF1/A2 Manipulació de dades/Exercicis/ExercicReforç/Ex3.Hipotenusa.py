"""
Exercici 3
Donats els catets a i b d'un triangle rectangle, escriure el codi Python que calcula la seva hipotenusa.
Cal recordar que la hipotenusa es calcula de la següent manera (Teorema de Pitàgores):

c2 = a2 + b2 , on c és la hipotenusa. Per tant,  c = √(a2 + b2)
"""
import math

a = int(input("dame un numero para el valor a: "))
b = int(input("dame un numero para el valor b: "))

c = math.sqrt(a**2 + b**2)
print("El resultat es: ", c)
