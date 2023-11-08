"""
Rene Tubiera
Exercici 14
Donat un nombre de dues xifres, escriu el programa que permet mostrar el nombre de manera “invertida”.
Per exemple, si l'usuari n'introdueix 14, el programa n'hauria de mostrar 41.

"""

"""
numero = int(input("Donam un numero: "))
digits = numero.count(numero)
print(numero[0-digits])
"""

numero = input("Dame un número de dos dígitos: ")

if len(numero) == 2:
    numero_invertido = numero[1] + numero[0]
    print("El número invertido es:", numero_invertido)
else:
    print("Por favor, introduce un número de dos dígitos.")
