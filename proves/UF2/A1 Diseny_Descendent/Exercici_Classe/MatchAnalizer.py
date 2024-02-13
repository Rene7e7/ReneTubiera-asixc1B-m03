'''
Rene Tubiera Sadinas
UF2
A1
Volem fer un programa que analitzi els resultats d'un partit de bàsquet. Hem de tenir en compte que en un partit de bàsquet es poden fer 1, 2 o 3 punts.

Donat els diferents resultats analitza que està passant.
0 2

0 5

2 5

3 5

3 7

-1
L'usuari introduirà primer el nom dels dos equips i després el resultat actual
'''
# Obtenir els noms dels equips
equip_local = input()
equip_visitant = input()
# diferents resultats
a = 0
b = 0
Inicio_puntuacio = (a,b)

puntuacio = input()

# region Equip
def equip():
    equip_local = input()
    equip_visitant = input()
# endregion
# region puntuacio
def puntuacio_partit():
    Puntuacio_A = []
    Puntuacio_B = []

    # Definimos las puntuaciones anteriores
    puntuacio_anterior_A = 0
    puntuacio_anterior_B = 0

    while True:
        entrada = input(
            "Introduce la puntuación de A seguida de la puntuación de B (separadas por un espacio), o bien introduce -1 para finalizar: ")
        puntuacio = entrada.split()
        if len(puntuacio) >= 2:
            # Si la puntuación no es -1, actualizamos la puntuación anterior
            if puntuacio[0] != '-1':
                puntuacio_anterior_A = int(puntuacio[0])
            if puntuacio[1] != '-1':
                puntuacio_anterior_B = int(puntuacio[1])

            # Añadimos las puntuaciones a las listas
            Puntuacio_A.append(puntuacio_anterior_A)
            Puntuacio_B.append(puntuacio_anterior_B)

            # Si se introduce -1, salimos del bucle
            if puntuacio[0] == '-1':
                break
        else:
            print("Por favor, introduce dos puntuaciones separadas por un espacio.")

# endregion
# region Resultat
def resulta():
    Resultat_A = []
    Resultat_B = []

# endregion
# region Guanyador
def guanyador():
    pass
# endregion

# region Funcions
equip()
resulta()
guanyador()
puntuacio_partit()

'''
puntos == 3:
    print("Es un triple)
puntos == 2:
    print("Es una cistella)
puntos == 1:
    print("Es un punto de tir lliure)
'''