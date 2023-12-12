# Solicitar la base y el exponente al usuario
try:
    base = int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))

    # Inicializar el resultado a 1
    resultado = 1

    # Calcular la potencia utilizando un bucle for
    for _ in range(exponente):
        resultado *= base

    # Imprimir el resultado
    print(f"El resultado de {base}^{exponente} es: {resultado}")

except ValueError:
    print("Debes ingresar enteros válidos para la base y el exponente.")
