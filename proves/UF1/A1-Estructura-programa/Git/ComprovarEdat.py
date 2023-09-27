"""
Rene Tubiera
M03 UF1
21/09/2023
Exercici 2 Comprovar Edat
"""
try:
    # Programa que demana l'edat i diu si ets major d'edat.
    edat = int(input("Quina edat tens? "))

    # Comprova si tens més de 18 anys
    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat ")

    print("Programa Finalitzat")
except ValueError:
    print("ERROR: Valor no valid")