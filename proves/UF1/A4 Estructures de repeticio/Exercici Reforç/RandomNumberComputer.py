
import random

try:
    contador = 0
    numero_secreto = int(input("Dime numero: "))
    num_computadora = random.randint(0,100)

    while num_computadora != numero_secreto or contador != 10:
        contador += 1

        usuario = input("El numero que has pensat es mes gran? ")
        if
            if num_computadora < numero_secreto:
                print("El numero es mas grande")
            if num_computadora > numero_secreto:
                print("El numero es mas pequeño")
    print("Pograma terminado")
except ValueError:
    print("Tiene que ser numeros enteros!")



