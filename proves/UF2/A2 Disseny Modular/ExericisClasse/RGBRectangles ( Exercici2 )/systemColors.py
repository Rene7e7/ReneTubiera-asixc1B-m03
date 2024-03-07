'''
Rene Tubiera
UF2 A2 Disseny modulars
'''

import colors
import os

color, fila, columna = input("Introdueix el color, fila i columna: ").split()

def dibujar_rectangulo(color, fila, columna):
    os.system('clear')
    for i in range(int(fila)):
        for j in range(int(columna)):
            print(color + 'X', end='')
        print()
def pintar_rectangulo(color, fila, columna):
    os.system('clear')
    for i in range(int(fila)):
        for j in range(int(columna)):
            # printa la X amb el color indicat
            print(color + 'X', end='')
    print(colors.FEND)