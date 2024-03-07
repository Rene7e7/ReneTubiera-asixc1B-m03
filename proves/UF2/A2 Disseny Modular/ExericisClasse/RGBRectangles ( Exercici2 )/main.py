'''
Rene Tubiera
UF2 A2 Disseny modulars
'''

import colors
import systemColors

def main():
    color, fila, columna = input("Introdueix el color, fila i columna: ").split()
    systemColors.pintar_rectangulo(color, fila, columna)
main()