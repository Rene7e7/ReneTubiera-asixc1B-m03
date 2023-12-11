"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
 Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
"""
# Tamaño del tablero
MIDA = 8

# Bucles anidados para recorrer cada fila y columna del tablero
for i in range(MIDA):
    for j in range(MIDA):
        # Si la suma de i y j es par, el cuadrado es blanco, de lo contrario es negro
        if (i + j) % 2 == 0:
            casillas = "██"
        else:
            casillas = "  "

        # Imprime el contenido del cuadrado actual sin saltar de línea
        print(casillas, end=" ")

    # Después de imprimir una fila completa, salta a la siguiente línea
    print()

"""
#MODELO HECHO POR RENE
BLANC = "⬜"
NEGRE = "⬛"
for i in range(8):
    filas = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            filas += NEGRE
        else:
            filas += BLANC
    print(filas)
"""
