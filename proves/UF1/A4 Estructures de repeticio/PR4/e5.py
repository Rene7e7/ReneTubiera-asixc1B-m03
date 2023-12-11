"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
e5. Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes
"""
try:
    # Inicialización de variables
    resultado = 0

    # Solicita al usuario que ingrese dos números
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    # Verifica si los números son positivos
    if num1 < 0 or num2 < 0:
        print("Esta calculadora funciona solo con números positivos.")
    else:
        # Bucle para realizar la multiplicación
        for i in range(num2):
            resultado += num1
            # La multiplicación es básicamente sumar el número 1 'num2' veces

        # Imprime el resultado de la multiplicación
        print("El resultado de", num1, "x", num2, "es:", resultado)

except ValueError:
    # Captura el error si la entrada no es un número entero
    print("Error: Debes ingresar un número entero.")
