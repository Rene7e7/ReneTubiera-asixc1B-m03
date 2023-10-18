"""
Implementa un programa que demani per teclat dos punts del pla i tot seguit calculi i mostri la distància entre ells.

Notes:

Un punt del pla es representa amb un parell de números. Per exemple, el punt A es representarà pels números x1 i y1, i el punt B pels números x2 i y2
La fórmula de la distància entre dos punts A i B és:

distància(A,B) = √( (x2 - x1)2 + (y2 - y1)2)

"""
import math
PuntAy = int(input("Dame un numero para el PuntAy: "))
PuntAx = int(input("Dame un numero para el PuntAx: "))
PuntBx = int(input("Dame un numero para el PuntBx: "))
PuntBy = int(input("Dame un numero para el PuntBy: "))

distanciaAB = math.sqrt((PuntAx - PuntBx)**2 + (PuntAy - PuntBy)**2)

print("El Resulytat es:", distanciaAB)