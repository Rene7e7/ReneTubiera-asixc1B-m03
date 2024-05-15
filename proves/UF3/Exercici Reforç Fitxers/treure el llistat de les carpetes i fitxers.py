'''
Exercici 2
Demanem a l’usuari un directori, hem de treure el llistat de les carpetes i fitxers del directori
'''

# region imports
import os
# endregion imports

# region functions
def llistar_directori(directori):
    # comprovar si el directori existeix
    if os.path.exists(directori):
        # comprovar si és un directori
        if os.path.isdir(directori):
            # llistar els fitxers i carpetes del directori
            print(f"Llistat de fitxers i carpetes de {directori}:")
            for element in os.listdir(directori):
                print(element)
        else:
            print(f"{directori} no és un directori.")
    else:
        print(f"El directori {directori} no existeix.")