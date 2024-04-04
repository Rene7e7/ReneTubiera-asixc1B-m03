'''
Rene Tubiera Sadinas
4/4/2024
M03 UF2 A1 i A2 pp1B - Prova Practica 1
ASIX1B
'''

def VocalsiConsonantes():
    try:
        data = str(input(
            "Por favor, escribe una oración: "))  # Solicita al usuario que ingrese una oración y la guarda en la variable 'data'
        vocals = "aeiou"  # Cadena que contiene las vocales
        for v in vocals:  # Bucle que recorre cada vocal en la cadena 'vowels'
            print(v, data.lower().count(v))  # Imprime la vocal actual y la cuenta de esa vocal en la oración (ignorando mayúsculas/minúsculas)
        consonantes = "qwrtyypsdfghjklñzxcvbnm"  # Cadena que contiene las vocales
        for v in consonantes:  # Bucle que recorre cada vocal en la cadena 'vowels'
            print(v, data.lower().count(v))  # Imprime la vocal actual y la cuenta de esa vocal en la oración (ignorando mayúsculas/minúsculas)
    except ValueError:
        print("Error")

def posicio():
    '''
    Donada una paraula i un valor indica quina lletra hi ha a la posició indicada
    Els strings funcionen com si fossin llistes de chars
    '''
    # Llegir la paraula i la posició
    paraula, posicio = input().split()
    # Convertir la posició a un nombre enter
    posicio = int(posicio)

    # Imprimir la lletra a la posició indicada
    print(paraula[posicio])


def Utilitat2():
    data = str(input("Por favor, escribe una oración: "))  # Solicita al usuario que ingrese una oración y la guarda en la variable 'data'
    print()

Utilitat2()