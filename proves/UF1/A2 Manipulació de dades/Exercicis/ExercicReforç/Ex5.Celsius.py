"""
Exercici 5
Realitza un programa que demani a l'usuari graus Fahrenheit i posteriorment els mostri com graus Celsius.

La fórmula per a la conversió és:

C = (F-32)*5/9
"""

grausFahrenheit = int(input("Dame un numero para graus Fahrenheit: "))
C = (grausFahrenheit-32) * 5 / 9
print("El resultat es: ", C)
