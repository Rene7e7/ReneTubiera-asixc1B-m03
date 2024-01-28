'''
e3.py
Escriu un programa que demani números per teclat fins que s'introdueix un zero.
El programa haurà d'imprimir la suma i la mitjana de tots els números introduïts.

'''
try:
    suma = 0
    contador = 0
    numero_usuario = 1  # Inicializamos con un valor diferente de 0 para que entre en el bucle

    while numero_usuario != 0:
        numero_usuario = int(input("Dime un número (introduce 0 para salir): "))

        if numero_usuario != 0:
            suma += numero_usuario
            contador += 1

    if contador > 0:
        # Calcular la media solo si se han introducido números
        media = suma / contador
        print(f"La suma de los números es: {suma}")
        print(f"La media de los números es: {media}")
    else:
        print("No se introdujeron números.")

except ValueError:
    print("Error: Debes ingresar números enteros.")
