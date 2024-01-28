'''
e5.py
Escriu un programa que demani per teclat lletres, d’una en una, fins que l’usuari entri un espai en blanc. Per cada lletra entrada,
el programa comprovarà si es tracta d’una vocal. Si ho és, escriurà en pantalla ‘VOCAL’. En cas contrari, ‘NO VOCAL’ (aquest cas inclou caràcters que no siguin lletres)
Nota: si l’usuari entra més d’una lletra (és a dir, una paraula o una frase), el programa ignorarà l’entrada i simplement tornarà  a demanar una lletra.
'''

try:
    # Inicializar listas
    VOCAL = []  # Lista para almacenar vocales
    NO_VOCAL = []  # Lista para almacenar no vocales

    lletres = input("Dime una letra (o introduce un espacio en blanco para salir): ")

    while not lletres.isspace():
        # Verificar si es una letra y es vocal
        if lletres.isalpha() and lletres.lower() in "aeiou":
            VOCAL.append(lletres)
        else:
            NO_VOCAL.append(lletres)

        # Volver a solicitar una letra
        lletres = input("Dime otra letra (o introduce un espacio en blanco para salir): ")

    # Imprimir resultados
    print("Vocales ingresadas:")
    for vocal in VOCAL:
        print(vocal, end=" ")

    print("\nNo vocales ingresadas:")
    for no_vocal in NO_VOCAL:
        print(no_vocal, end=" ")

except ValueError:
    print("Error: Debes ingresar letras.")
