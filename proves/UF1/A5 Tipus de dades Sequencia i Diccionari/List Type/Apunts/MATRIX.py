MIDA = 4
matrix = [[0] * MIDA for i in range(MIDA)]
for fila in range(MIDA):
   for columna in range(MIDA):
       if fila < columna:
           matrix[fila][columna] = 0
       elif fila > columna:
           matrix[fila][columna] = 0
       else:
           matrix[fila][columna] = 1
for fila in matrix:
   print(' '.join([str(elem) for elem in fila]))
