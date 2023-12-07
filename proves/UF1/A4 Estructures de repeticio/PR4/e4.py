"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
 Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
"""
# Hecho por los dos
# Los rangos de un cuadrado de 8x8
MIDA=8
for i in range(MIDA):
    for j in range(MIDA):
# Si son divisibles la suma de i+j seran las blancas porque son el comienzo
# Ejemplo el primer cuadrado del tablero (arriba a la izquierda) sus coordenadas son i(x)=1 j(y)=1 -> 1+1=2/2=0
        if (i + j) % 2 == 0:
            casillas = "██"
        else:
            casillas = "  "
# Este print de abajo es para que salte a la siguiente linea y el otro print es pura estetica
        print(casillas, end=" ")
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