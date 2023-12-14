try:
    # Inicializar listas
    VOCAL = []  # Lista para almacenar vocales
    NO_VOCAL = []  # Lista para almacenar no vocales

    while True:
        lletres = input("Dime una letra (o introduce un espacio en blanco para salir): ")

        # Verificar si la cadena es vacía para salir del bucle
        if not lletres:
            # Imprimir resultados y salir del bucle
            print("Vocales ingresadas:")
            for vocal in VOCAL:
                print(vocal, end=" ")

            print("\nNo vocales ingresadas:")
            for no_vocal in NO_VOCAL:
                print(no_vocal, end=" ")

            break

        # Verificar si es una vocal
        if lletres.lower() in "aeiou":
            VOCAL.append(lletres)
        else:
            NO_VOCAL.append(lletres)

except ValueError:
    print("Error: Debes ingresar letras.")
