try:
    numero_1 = int(input("Dime el primer numero: "))
    numero_2 = int(input("Dime el segundo numero: "))

    # Asegurarse de que el límite inferior es menor que el superior
    while numero_1 >= numero_2:
        print("El límite inferior debe ser menor que el superior.")
        numero_1 = int(input("Dime el primer numero: "))
        numero_2 = int(input("Dime el segundo numero: "))

    suma_intervalo = 0
    numeros_dentro_intervalo = []
    numeros_fuera_intervalo = []
    ha_ingresado_limites = False

    numero = int(input("Dime un numero (introduce 0 para salir): "))

    while numero != 0:
        if numero == numero_1 or numero == numero_2:
            ha_ingresado_limites = True
        elif numero > numero_1 and numero < numero_2:
            suma_intervalo += numero
            numeros_dentro_intervalo.append(numero)
        else:
            numeros_fuera_intervalo.append(numero)

        numero = int(input("Dime otro numero (introduce 0 para salir): "))

    print("\nResultados:")
    print("Números dentro del intervalo:", numeros_dentro_intervalo)
    print("Números fuera del intervalo:", numeros_fuera_intervalo)
    print("La suma de los números dentro del intervalo es:", suma_intervalo)
    print("Cantidad de números fuera del intervalo:", len(numeros_fuera_intervalo))
    print("¿Se ha ingresado algún número igual a los límites del intervalo?", ha_ingresado_limites)

except ValueError:
    print("Error: Debes ingresar números enteros.")
