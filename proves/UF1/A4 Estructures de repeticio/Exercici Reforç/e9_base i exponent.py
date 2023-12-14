try:
    # Pedir al usuario que ingrese la base y el exponente
    base = int(input("Introduce la base (número entero): "))
    exponente = int(input("Introduce el exponente (número entero positivo o cero): "))

    # Asegurarse de que el exponente sea positivo o cero
    while exponente < 0:
        print("El exponente debe ser positivo o cero.")
        exponente = int(input("Introduce el exponente (número entero positivo o cero): "))

    # Inicializar el resultado a 1 (cualquier número elevado a 0 es 1)
    resultado = 1

    # Calcular la potencia utilizando un bucle for
    for _ in range(exponente):
        resultado *= base

    # Mostrar el resultado
    print(f"El resultado de {base}^{exponente} es: {resultado}")

except ValueError:
    print("Error: Debes ingresar números enteros.")
