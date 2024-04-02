import random

def crear_tablero(filas, columnas, minas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    minas_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    crear_minas(tablero, minas_tablero, filas, columnas, minas)
    return tablero, minas_tablero

def crear_minas(tablero, minas_tablero, filas, columnas, minas):
    minas_creadas = 0
    while minas_creadas < minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if minas_tablero[fila][columna] != -1:
            minas_tablero[fila][columna] = -1
            minas_creadas += 1
            actualizar_alrededor(tablero, minas_tablero, fila, columna, filas, columnas)

def actualizar_alrededor(tablero, minas_tablero, fila, columna, filas, columnas):
    for i in range(-1, 2):
        for j in range(-1, 2):
            nueva_fila = fila + i
            nueva_columna = columna + j
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                if minas_tablero[nueva_fila][nueva_columna] != -1:
                    minas_tablero[nueva_fila][nueva_columna] += 1

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(x) for x in fila))

def jugar_buscamines():
    print("Benvingut al joc del 'buscamines'!")
    filas = int(input("Introdueix el nombre de files del taulell: "))
    columnas = int(input("Introdueix el nombre de columnes del taulell: "))
    minas = int(input("Introdueix el nombre de mines: "))

    tablero, minas_tablero = crear_tablero(filas, columnas, minas)
    jugar(filas, columnas, minas_tablero, tablero)

def jugar(filas, columnas, minas_tablero, tablero):
    while True:
        mostrar_tablero(tablero)
        fila = int(input("Introdueix la fila (0 a {}): ".format(filas - 1)))
        columna = int(input("Introdueix la columna (0 a {}): ".format(columnas - 1)))

        if minas_tablero[fila][columna] == -1:
            print("Has perdut! Hi ha una mina en aquesta posició.")
            tablero[fila][columna] = 'X'
            mostrar_tablero(tablero)
            break
        else:
            tablero[fila][columna] = str(minas_tablero[fila][columna])

if __name__ == "__main__":
    jugar_buscamines()
