'''
Implementar un programa, que:
Crea una taula bidimensional de longitud 5x15
Carrega la taula amb únicament zeros i uns, on els uns ocuparan les posicions o elements que delimiten la taula, és a dir, les més externes, mentre que la resta dels elements contindran zeros.
Mostra el contingut de la matriu a la pantalla, és a dir, mostra el següent:
111111111111111
100000000000001
100000000000001
100000000000001
111111111111111

'''


columna = 15
filas = 5


if columna <= 0 or filas <= 0:
    print("Error")
else:
    for i in range(filas):
        for j in range(columna):
            if i == 0 or i == filas - 1 or j == 0 or j == columna - 1:
                print("1", end=" ")
            else:
                print("0", end=" ")  # Espacios para el interior de la caja
        print()
