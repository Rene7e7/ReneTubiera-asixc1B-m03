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
# region Equips
def equips():
    equip1 = input("Introdueix el nom del primer equip: ")
    equip2 = input("Introdueix el nom del segon equip: ")

    punts_equip1 = 0
    punts_equip2 = 0
    while True:
        try:
            punts_equip1, punts_equip2 = map(int, input(f"Introdueix els punts ({equip1} {equip2}): ").split())
            if punts_equip1 == -1 or punts_equip2 == -1:
                break
        except ValueError:
            print("Per favor, introdueix dos nombres separats per un espai.")
            break
# endregion

# region puntuacio
def puntuacio():
    pass
# endregion
equips()
puntuacio()