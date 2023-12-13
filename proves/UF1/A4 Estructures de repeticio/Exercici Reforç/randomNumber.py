'''
Rene Tubiera
ASIXc1B

Crea una aplicació que permet
 endevinar un número. L'aplicació genera un nombre “aleatori” de l'1 al 100. A continuació,
 l’aplicació va demanant números i va responent si el nombre a endevinar és més gran o
 més petit que el que ha introduït, a més dels intents que et queden (tens 10 intents per encertar-lo).
 El programa acaba quan s'encerta el número (a més et diu quants intents has necessitat per encertar-lo),
 si s'arriba al límit d'intents, l’aplicació et mostra el número que havia generat.
Pista: randint '''

import random

try:
    numero_secrero = random.randint(0,100)
    contador = 0
    print(numero_secrero)
    for i in range (10):
        numero = int(input("Dime numero: "))
        if numero != numero_secrero:
            contador += 1
            print("Intentalo de nuevo")
            print("Numero intentos: ",contador)
        else:
            print("Has acertado")


        if numero < numero_secrero:
            print("El numero es mas grande")
        if numero > numero_secrero:
            print("El numero es mas pequeño")
    print("Pograma terminado")



except ValueError:
    print("Tiene que ser numeros enteros!")


''' FOR 
import random

try:
    numero_secrero = random.randint(0,100)
    contador = 0
    print(numero_secrero)
    for i in range (10):
        numero = int(input("Dime numero: "))
        if numero != numero_secrero:
            contador += 1
            print("Intentalo de nuevo")
            print("Numero intentos: ",contador)
        else:
            print("Has acertado")


        if numero < numero_secrero:
            print("El numero es mas grande")
        if numero > numero_secrero:
            print("El numero es mas pequeño")
    print("Pograma terminado")



except ValueError:
    print("Tiene que ser numeros enteros!")
'''