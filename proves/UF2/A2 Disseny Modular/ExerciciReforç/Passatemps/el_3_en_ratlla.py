# Implementación básica del juego 3 en Raya en Python

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def jugar_tic_tac_toe():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        mostrar_tablero(tablero)
        fila, columna = map(int, input(f"Turno de {jugador_actual}. Ingresa fila (1-3) y columna (1-3): ").split())
        tablero[fila - 1][columna - 1] = jugador_actual

        # Verificar si hay un ganador o empate
        # Implementa la lógica aquí

        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar_tic_tac_toe()
