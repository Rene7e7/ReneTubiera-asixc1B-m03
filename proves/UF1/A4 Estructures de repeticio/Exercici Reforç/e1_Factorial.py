try:
    # Solicitar al usuario ingresar un número
    num = int(input("Introduce un número para calcular su factorial: "))

    # Verificar si el número es no negativo
    if num >= 0:
        factorial = 1  # Inicializamos el factorial a 1

        # Bucle for para calcular el factorial
        for i in range(1, num + 1):
            factorial *= i  # Multiplicamos el factorial por cada número del 1 a num

        # Imprimir el resultado
        print(f"El factorial de {num} es: {factorial}")
    else:
        print("Ingresa un número no negativo.")

except ValueError:
    print("Debes ingresar un número entero.")

