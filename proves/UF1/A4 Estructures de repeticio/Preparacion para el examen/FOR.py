# Ejercicio 1: Suma de Números Pares
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima la suma de los números pares desde 1 hasta N.

numero = int(input("Dime un numero: "))
for i in range(1,numero,):
    for j in range(1,10,2):
        print(f"{i}+{j} =",i+j)
print("--------------")

# Ejercicio 2: Tabla de Multiplicar
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima la tabla de multiplicar del 1 al 10 para ese número.
numero = int(input("Dime un numero: "))
for i in range(1,numero,):
    for j in range(1,10):
        print(f"{i}x{j} =",i*j)
print("--------------")

# Ejercicio 3: Contador Regresivo
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima un contador regresivo desde N hasta 1.
numero = int(input("Dime un numero: "))
for var in range(10,numero,-1):
    print(var," ",end="")

# Ejercicio 4: Factorial
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima el factorial de ese número.
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


# Ejercicio 5: Números Primos
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima si ese número es primo o no.
try:
    # Solicitar al usuario ingresar un número
    num = int(input("Introduce un número para verificar si es primo: "))

    # Verificar si el número es mayor que 1
    if num > 1:
        es_primo = True  # Suponemos que el número es primo

        # Bucle for para comprobar la divisibilidad
        for i in range(2, num):
            if num % i == 0:
                es_primo = False  # Si es divisible por algún número, no es primo
                break

        # Imprimir el resultado
        if es_primo:
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
    else:
        print("Ingresa un número mayor que 1.")

except ValueError:
    print("Debes ingresar un número entero.")

# Ejercicio 6: Dibujo con For
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima un patrón con * y espacios que forme un triángulo.

numero = int(input("Dime un numero: "))
for i in range(1, numero + 1):
    espacio = numero - i
    estrellitas = 2 * i - 1
    print(' ' * espacio + '*' * estrellitas)

# Ejercicio 7: Suma de Dígitos
# Escribe un programa que solicite al usuario ingresar un número (N) y luego imprima la suma de sus dígitos.

try:
    # Solicitar al usuario ingresar un número
    numero = int(input("Introduce un número para calcular la suma de sus dígitos: "))

    # Verificar si el número es no negativo
    if numero >= 0:
        suma_digitos = 0  # Inicializamos la suma de dígitos a 0

        # Bucle for para calcular la suma de dígitos
        for digito in str(numero):
            suma_digitos += int(digito)  # Convertimos cada dígito a entero y lo sumamos

        # Imprimir el resultado
        print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
    else:
        print("Ingresa un número no negativo.")

except ValueError:
    print("Debes ingresar un número entero.")

# Ejercicio 8: Adivina el Número
# Escribe un programa que genere un número aleatorio entre 1 y 100. Luego, pide al usuario que adivine el número. Proporciona pistas (mayor, menor) hasta que el usuario adivine.

# Ejercicio 9: Serie Fibonacci
# Escribe un programa que solicite al usuario ingresar un número (N) e imprima los primeros N términos de la serie Fibonacci.

