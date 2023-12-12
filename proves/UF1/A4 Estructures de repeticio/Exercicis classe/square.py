try:
    # Solicitar el tamaño del cuadrado al usuario
    n = int(input("Introduce el tamaño del cuadrado: "))

    # Imprimir la parte superior del cuadrado
    print("#" * n)

    # Imprimir las filas interiores del cuadrado
    for i in range(n - 2):
        print("#" + " " * (n - 2) + "#")

    # Imprimir la parte inferior del cuadrado
    if n > 1:
        print("#" * n)

except ValueError:
    print("Debes ingresar un número entero para el tamaño del cuadrado.")
