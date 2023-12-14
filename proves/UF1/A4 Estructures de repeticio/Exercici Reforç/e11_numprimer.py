try:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Introduce un número entero positivo: "))

    # Verificar si el número es mayor que 1 (los números primos son mayores que 1)
    if numero <= 1:
        print("El número debe ser mayor que 1.")
    else:
        es_primo = True  # Suponemos que el número es primo inicialmente

        # Probar divisibilidad desde 2 hasta la raíz cuadrada del número
        i = 2
        while i <= int(numero**0.5) and es_primo:
            if numero % i == 0:
                es_primo = False  # Si es divisible, el número no es primo
            i += 1  # Pasar al siguiente número

        # Mostrar el resultado
        if es_primo:
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")

except ValueError:
    print("Error: Debes ingresar un número entero.")
