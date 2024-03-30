def crear_tablero(filas, columnas):
    return [[" " for _ in range(columnas)] for _ in range(filas)]

def agregar_minas(tablero, num_minas):
    # Implementa la lógica para agregar minas aleatoriamente al tablero
    # Aquí puedes usar algún algoritmo para distribuir las minas de manera aleatoria
    pass

def mostrar_tablero(tablero):
    # Implementa la lógica para mostrar el tablero actual
    for fila in tablero:
        print(" ".join(fila))

def abrir_casilla(tablero, fila, columna):
    # Implementa la lógica para abrir una casilla y verificar si hay mina
    if tablero[fila][columna] == "*":
        return True
    return False

def verificar_victoria(tablero):
    # Implementa la lógica para verificar si el jugador ha ganado
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

def jugar_buscamines():
    filas = 6
    columnas = 6
    num_minas = 6

    tablero = crear_tablero(filas, columnas)
    agregar_minas(tablero, num_minas)

    while True:
        mostrar_tablero(tablero)
        fila = int(input("Introduce la fila (0-{0}): ".format(filas - 1)))
        columna = int(input("Introduce la columna (0-{0}): ".format(columnas - 1)))

        if not (0 <= fila < filas) or not (0 <= columna < columnas):
            print("Posición inválida. Inténtalo de nuevo.")
            continue

        if abrir_casilla(tablero, fila, columna):
            print("¡Has perdido! ¡Había una mina!")
            break

        if verificar_victoria(tablero):
            print("¡Felicidades! ¡Has ganado!")
            break

if __name__ == "__main__":
    jugar_buscamines()
