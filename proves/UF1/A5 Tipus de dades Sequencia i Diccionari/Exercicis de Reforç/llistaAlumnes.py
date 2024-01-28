'''
e8.py
Volem desar els noms i les edats dels alumnes de curs. Feu un programa que introdueixi el nom i l'edat de cada alumne. El procés de lectura de dades acabarà quan s'introdueix com a nom un asterisc (*)
En finalitzar es mostrarà les dades següents:
Els alumnes majors d’edat
Els alumnes més vells: per fer això caldrà primer que obtingueu quina és l’edat més gran que us han entrat i aleshores mostrar els alumnes que tinguin aquesta edat (pot haver-hi més d’un)

'''

llista_noms = []
llista_edats = []

while True:
    nom = input("Digam el nom de l'alumne (o * per acabar): ")

    if nom == "*":
        break  # Si se ingresa "*", salimos del bucle

    try:
        edat = int(input(f"Digam l'edat de {nom}: "))
        llista_noms.append(nom)
        llista_edats.append(edat)
    except ValueError:
        print("Error: Si us plau, introdueix una edat vàlida.")

# Imprimir les llistes resultants
print("\nLlista de noms dels alumnes:", llista_noms)
print("Llista d'edats dels alumnes:", llista_edats)
