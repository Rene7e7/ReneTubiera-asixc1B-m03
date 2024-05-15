'''
Exercici 3:
Demanem a l’usuari un directori d’origen, o bé un arxiu, i hem de poder crear un directori o un fitxer, esborrar-lo, canviar-li el nom i canviar els permisos
'''

# region imports
import os
# endregion imports

# region functions
def crear_directori_fitxer():
    # demanar el directori o fitxer d'origen
    origen = input("Introdueix el directori o fitxer d'origen: ")
    # comprovar si el directori o fitxer d'origen existeix
    if os.path.exists(origen):
        # demanar si es vol crear un directori o un fitxer
        tipus = input("Vols crear un directori o un fitxer? (d/f): ")
        # comprovar si es vol crear un directori
        if tipus == "d":
            # demanar el nom del directori
            nom_directori = input("Introdueix el nom del directori: ")
            # crear el directori
            os.mkdir(os.path.join(origen, nom_directori))
            print(f"Creat el directori {nom_directori} a {origen}.")
        # comprovar si es vol crear un fitxer
        elif tipus == "f":
            # demanar el nom del fitxer
            nom_fitxer = input("Introdueix el nom del fitxer: ")
            # crear el fitxer
            open(os.path.join(origen, nom_fitxer), "w").close()
            print(f"Creat el fitxer {nom_fitxer} a {origen}.")
        else:
            print("Opció incorrecta.")
    else:
        print(f"El directori o fitxer {origen} no existeix.")

def esborrar_directori_fitxer():
    # demanar el directori o fitxer d'origen
    origen = input("Introdueix el directori o fitxer d'origen: ")
    # comprovar si el directori o fitxer d'origen existeix
    if os.path.exists(origen):
        # comprovar si es vol esborrar un directori
        if os.path.isdir(origen):
            os.rmdir(origen)
            print(f"Esborrat el directori {origen}.")
        # comprovar si es vol esborrar un fitxer
        elif os.path.isfile(origen):
            os.remove(origen)
            print(f"Esborrat el fitxer {origen}.")
        else:
            print(f"{origen} no és ni un directori ni un fitxer.")
    else:
        print(f"El directori o fitxer {origen} no existeix.")

def canviar_nom_directori_fitxer():
    # demanar el directori o fitxer d'origen
    origen = input("Introdueix el directori o fitxer d'origen: ")
    # comprovar si el directori o fitxer d'origen existeix
    if os.path.exists(origen):
        # demanar el nou nom
        nou_nom = input("Introdueix el nou nom: ")
        # canviar el nom del directori o fitxer
        os.rename(origen, nou_nom)
        print(f"Canviat el nom de {origen} a {nou_nom}.")
    else:
        print(f"El directori o fitxer {origen} no existeix.")

def canviar_permisos_directori_fitxer():
    # demanar el directori o fitxer d'origen
    origen = input("Introdueix el directori o fitxer d'origen: ")
    # comprovar si el directori o fitxer d'origen existeix
    if os.path.exists(origen):
        # demanar els permisos
        permisos = input("Introdueix els permisos (en format octal): ")
        # canviar els permisos del directori o fitxer
        os.chmod(origen, int(permisos, 8))
        print(f"Canviats els permisos de {origen} a {permisos}.")
    else:
        print(f"El directori o fitxer {origen} no existeix.")
# endregion functions

# region main
if __name__ == '__main__':
    opcio = ""
    while opcio != "5":
        print("\nExercici 3:")
        print("1 - Crear directori o fitxer")
        print("2 - Esborrar directori o fitxer")
        print("3 - Canviar nom de directori o fitxer")
        print("4 - Canviar permisos de directori o fitxer")
        print("5 - Sortir")

        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            crear_directori_fitxer()
        elif opcio == "2":
            esborrar_directori_fitxer()
        elif opcio == "3":
            canviar_nom_directori_fitxer()
        elif opcio == "4":
            canviar_permisos_directori_fitxer()
        elif opcio == "5":
            break
        else:
            print("Opció incorrecta.")
# endregion main


