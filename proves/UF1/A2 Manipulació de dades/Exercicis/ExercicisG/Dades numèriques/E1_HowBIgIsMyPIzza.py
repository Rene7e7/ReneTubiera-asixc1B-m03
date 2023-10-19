"""
11/10/2023
René Tubiera y Jordi Yu

E1. HowBigIsMyPizza
Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície.
Pots usar Math.PI per escriure el valor de Pi.

"""
import math
# importa math es para activar funciones matematicas

# Pedimos a l'usuarió el diametro para calcular la superficie
Diametro = int(input("Dime el diametro (en cm) de la pizza: "))

Superficie = math.pi*((Diametro/2)**2)
print("Este es tu resultado de la superficie de tu pizza",Superficie, "cm")
