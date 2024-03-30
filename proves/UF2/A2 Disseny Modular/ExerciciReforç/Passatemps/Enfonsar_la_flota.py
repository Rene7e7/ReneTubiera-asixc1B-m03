def crear_tablero(filas, columnas):
    return [[" " for _ in range(columnas)] for _ in range(filas)]

def agregar_barcos(tablero):
    # Implementa la lógica para agregar barcos al tablero
    # Puedes pedir al usuario que indique las posiciones de los barcos
    pass

def mostrar_tablero(tablero):
    # Implementa la lógica para mostrar el tablero actual
    for fila in tablero:
        print(" ".join(fila))

def disparar(tablero, fila, columna):
    # Implementa la lógica para disparar a una casilla y verificar si hay un barco
    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"  # Marcar como hundido
        return True
    else:
        tablero[fila][columna] = "-"  # Marcar como agua
        return False

def verificar_victoria(tablero):
    # Implementa la lógica para verificar si todos los barcos han sido hundidos
    for fila in tablero:
        for casilla in fila:
            if casilla == "B":
                return False
    return True

def jugar_hundir_la_flota():
    filas = 10
    columnas = 10

    tablero = crear_tablero(filas, columnas)
    agregar_barcos(tablero)

    while True:
        mostrar_tablero(tablero)
        fila = int(input("Introduce la fila (0-{0}): ".format(filas - 1)))
        columna = int(input("Introduce la columna (0-{0}): ".format(columnas - 1)))

        if not (0 <= fila < filas) or not (0 <= columna < columnas):
            print("Posición inválida. Inténtalo de nuevo.")
            continue

        if disparar(tablero, fila, columna):
            print("¡Has hundido un barco!")
        else:
            print("Agua. Sigue intentándolo.")

        if verificar_victoria(tablero):
            print("¡Felicidades! ¡Has hundido todos los barcos!")
            break

if __name__ == "__main__":
    jugar_hundir_la_flota()
