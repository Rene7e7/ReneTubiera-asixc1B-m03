'''
e11.py
Escriu un programa, que:
Crea una taula o matriu bidimensional de longitud 5x5 i nom diagonal
Assigna a cada casella de la matriu el valor 0 o 1 de la manera següent: les caselles pertanyents a  les dues diagonals majors de la matriu prenen el valor 1 i la resta de les caselles el valor 0
Mostra el contingut de la matriu a la pantalla.
Sortida del programa per pantalla:
1  0  0  0  1
0  1  0  1  0
0  0  1  0  0
0  1  0  1  0
1  0  0  0  1

'''
MIDA = 5
matrix = [[0] * MIDA for i in range(MIDA)]
for fila in range(MIDA):
    for columna in range(MIDA):
        if fila == columna or fila == MIDA - 1 - columna:
            matrix[fila][columna] = 1
        else:
            matrix[fila][columna] = 0

for fila in matrix:
    print(' '.join([str(elem) for elem in fila]))
