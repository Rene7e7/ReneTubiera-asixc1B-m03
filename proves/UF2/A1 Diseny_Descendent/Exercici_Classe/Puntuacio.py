Puntuacio_A = []
Puntuacio_B = []

# Definimos las puntuaciones anteriores
puntuacio_anterior_A = 0
puntuacio_anterior_B = 0

while True:
    entrada = input(
        "Introduce la puntuación de A seguida de la puntuación de B (separadas por un espacio), o bien introduce -1 para finalizar: ")
    puntuacio = entrada.split()
    if len(puntuacio) >= 2:
        # Si la puntuación no es -1, actualizamos la puntuación anterior
        if puntuacio[0] != '-1':
            puntuacio_anterior_A = int(puntuacio[0])
        if puntuacio[1] != '-1':
            puntuacio_anterior_B = int(puntuacio[1])

        # Añadimos las puntuaciones a las listas
        Puntuacio_A.append(puntuacio_anterior_A)
        Puntuacio_B.append(puntuacio_anterior_B)

        # Si se introduce -1, salimos del bucle
        if puntuacio[0] == '-1':
            break
    else:
        print("Por favor, introduce dos puntuaciones separadas por un espacio.")

