'''
Escriure un programa que:
Crea una taula (llista amb dues dimensions) de 5x5 nombres enters
Llegeix per teclat els nombres enters per a cada casella de la taula
Mostra per pantalla la suma de tots els elements de cada fila i la suma de tots els elements de cada columna
Pista: una taula es pot veure com una llista de llistes.

'''

# Crear una tabla (lista con dos dimensiones) de 5x5 números enteros
tabla = []
for indice_fila in range(1, 6):
    fila = []
    for indice_col in range(1, 6):
        fila.append(int(input("Introduce el número para la fila " + str(indice_fila) + " y columna " + str(indice_col) + ": ")))
    tabla.append(fila)

# Mostrar la tabla
print("Tabla:")
for fila in tabla:
    print(fila)

# Calcular la suma de cada fila
indice_fila = 1
for fila in tabla:
    suma_fila = sum(fila)
    print("La suma de los elementos de la fila " + str(indice_fila) + " es " + str(suma_fila))
    indice_fila += 1

# Calcular la suma de cada columna
indice_col = 1
for indice_col in range(1, 6):
    suma_col = sum(tabla[indice_fila - 1][indice_col - 1] for indice_fila in range(1, 6))
    print("La suma de los elementos de la columna " + str(indice_col) + " es " + str(suma_col))
    indice_col += 1

