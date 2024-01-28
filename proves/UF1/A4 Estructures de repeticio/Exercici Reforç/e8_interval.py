'''
Implementa un programa que demani dos números: un serà el límit inferior d’un interval i l’altre el límit superior. Si el límit inferior és més gran que el superior ho ha de tornar a demanar.
A continuació el programa demanarà per teclat números fins que introduïm el 0. Quan acabi el programa donarà la informació següent:
La suma dels números que estan dins de l'interval SENSE ser cap dels valors indicats com a límit inferior o límit superior  (interval obert)
Quants números són fora de l'interval.
Informar de si hem introduït algun número que sigui igual al límit inferior o al límit superior de l'interval, o no.

'''
try:
    numero_1 = int(input("Dime el primer numero: "))
    numero_2 = int(input("Dime el segundo numero: "))

    # Asegurarse de que el límite inferior es menor que el superior
    while numero_1 >= numero_2:
        print("El límite inferior debe ser menor que el superior.")
        numero_1 = int(input("Dime el primer numero: "))
        numero_2 = int(input("Dime el segundo numero: "))

    suma_intervalo = 0
    cantidad_fuera_intervalo = 0
    ha_ingresado_limites = False
    numeros_ingresados = []

    numero = int(input("Dime un numero (introduce 0 para salir): "))

    while numero != 0:
        numeros_ingresados.append(numero)

        if numero == numero_1 or numero == numero_2:
            ha_ingresado_limites = True
        elif numero > numero_1 and numero < numero_2:
            suma_intervalo += numero
        else:
            cantidad_fuera_intervalo += 1

        numero = int(input("Dime otro numero (introduce 0 para salir): "))

    print("Números ingresados por el usuario:", numeros_ingresados)
    print("La suma de los números dentro del intervalo es:", suma_intervalo)
    print("Cantidad de números fuera del intervalo:", cantidad_fuera_intervalo)
    print("¿Se ha ingresado algún número igual a los límites del intervalo?", ha_ingresado_limites)

except ValueError:
    print("Error: Debes ingresar números enteros.")
