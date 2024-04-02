import random

def crear_tablero():
    tablero = [[' ' for _ in range(10)] for _ in range(10)]
    return tablero

def colocar_barcos(tablero):
    barcos = {'A': 5, 'B': 4, 'S': 3, 'D': 3, 'P': 2}
    for barco, longitud in barcos.items():
        while True:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(['horizontal', 'vertical'])
            if verificar_colocacion(tablero, fila, columna, longitud, orientacion):
                colocar_barco(tablero, fila, columna, longitud, orientacion, barco)
                break

def verificar_colocacion(tablero, fila, columna, longitud, orientacion):
    if orientacion == 'horizontal' and columna + longitud <= 10:
        for i in range(longitud):
            if tablero[fila][columna + i] != ' ':
                return False
        return True
    elif orientacion == 'vertical' and fila + longitud <= 10:
        for i in range(longitud):
            if tablero[fila + i][columna] != ' ':
                return False
        return True
    return False

def colocar_barco(tablero, fila, columna, longitud, orientacion, barco):
    if orientacion == 'horizontal':
        for i in range(longitud):
            tablero[fila][columna + i] = barco
    elif orientacion == 'vertical':
        for i in range(longitud):
            tablero[fila + i][columna] = barco

def mostrar_tablero(tablero):
    print("  0 1 2 3 4 5 6 7 8 9")
    for i in range(10):
        print(str(i) + " " + " ".join(tablero[i]))

def jugar_hundir_la_flota():
    print("Benvingut al joc 'Hundir la Flota'!")
    tablero = crear_tablero()
    colocar_barcos(tablero)
    jugar(tablero)

def jugar(tablero):
    while True:
        mostrar_tablero(tablero)
        fila = int(input("Introdueix la fila (0-9): "))
        columna = int(input("Introdueix la columna (0-9): "))
        if tablero[fila][columna] != ' ':
            print("Tocado!")
            tablero[fila][columna] = 'X'
        else:
            print("Aigua!")
            tablero[fila][columna] = '-'

if __name__ == "__main__":
    jugar_hundir_la_flota()

