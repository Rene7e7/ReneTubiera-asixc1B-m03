'''

'''
# Símbolo de la torre
TORRE = "♖"

# Entrada del usuario
posicion = input("Entra la posició de la torre (format: fila columna): ")
fila, letra_columna = posicion.split()
fila = int(fila) - 1  # Restar 1 porque los índices de las listas comienzan desde 0
columna = ord(letra_columna.lower()) - ord('a')  # Convertir la letra de la columna a número

# Crear un tablero de ajedrez 8x8 con valores iniciales de 0
tablero = [[0] * 8 for _ in range(8)]

# Marcar la posición de la torre con el símbolo TORRE (valor 2)
tablero[fila][columna] = TORRE

# Marcar las posiciones a lo largo de la fila y columna con el valor 1
for i in range(8):
    if i != fila:
        tablero[i][columna] = 1
    if i != columna:
        tablero[fila][i] = 1

# Mostrar el tablero
for fila_tablero in tablero:
    for casilla in fila_tablero:
        print("♖" if casilla == 2 else "1" if casilla == 1 else "x", end=" ")
    print()
