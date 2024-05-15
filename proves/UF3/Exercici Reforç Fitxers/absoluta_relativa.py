'''
Exercici 1
Demanem a l’usuari el nom d’un fitxer o d’una carpeta.
Cal indicar si existeix o no. En cas d’existir indicar
si es tracta d’un fitxer o d’un directori, i mostrar la
ruta absoluta i la relativa.

'''

# region imports
import os
# endregion imports

# region functions
nom_fitxer = input("Introdueix el nom d'un fitxer o carpeta: ")
if os.path.exists(nom_fitxer):
    # comprovar si és fitxer o carpeta
    if os.path.isfile(nom_fitxer):
        print(f"El fitxer {nom_fitxer} existeix.")
    elif os.path.isdir(nom_fitxer):
        print(f"La carpeta {nom_fitxer} existeix.")
    print(f"Ruta absoluta: {os.path.abspath(nom_fitxer)}")
    print(f"Ruta relativa: {os.path.relpath(nom_fitxer)}")

else:
    print(f"El fitxer o carpeta {nom_fitxer} no existeix.")
# endregion functions

