'''
e4.py
Programa que declara una llista i la va omplint de números fins
que introduïm un nombre negatiu (el qual no afegirem) Un cop fet
això, cal mostrar en pantalla tots els nombres de la llista.

'''

llista_numeros = []
numero = 0
while numero >= 0:
    numero = int(input("Introdueix un numero"))
    if numero >= 0:
        llista_numeros.append(numero)
print("Llista de números:", llista_numeros)
