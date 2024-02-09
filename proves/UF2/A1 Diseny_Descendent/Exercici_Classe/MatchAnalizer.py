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
    puntuacio_local = []
    puntuacio_visitant = []
    Punts = []
    while Punts != "-1":
        puntuacio = input()

# endregion
# region Resultat
def resulta():
    pass
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