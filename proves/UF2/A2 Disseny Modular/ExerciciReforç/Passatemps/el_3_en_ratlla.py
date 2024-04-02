def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador or \
           tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def jugar_tres_en_raya():
    print("Benvingut al joc del 'Tres en Raya'!")
    tablero = crear_tablero()
    jugador_actual = 'X'

    for _ in range(9):  # Máximo de 9 movimientos
        mostrar_tablero(tablero)
        fila = int(input("Introdueix la fila (0-2): "))
        columna = int(input("Introdueix la columna (0-2): "))

        # Verificar si la casilla está libre
        if tablero[fila][columna] != ' ':
            print("Aquesta casella ja està ocupada. Tria una altra.")
            continue

        # Colocar el símbolo del jugador en la casilla
        tablero[fila][columna] = jugador_actual

        # Verificar si el jugador actual ha ganado
        if verificar_ganador(tablero, jugador_actual):
            print("Felicidades! El jugador {} ha guanyat!".format(jugador_actual))
            break

        # Cambiar al siguiente jugador
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'
    else:
        print("Empat! No hi ha guanyadors.")

if __name__ == "__main__":
    jugar_tres_en_raya()
