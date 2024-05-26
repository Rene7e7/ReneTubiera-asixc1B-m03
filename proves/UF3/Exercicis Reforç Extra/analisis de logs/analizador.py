import os

def analitzar_log(ruta_fitxer, cadena):
    try:
        with open(ruta_fitxer, "r") as f:
            linies = f.readlines()
            coincidencies = [linia.strip() for linia in linies if cadena in linia]
            return len(coincidencies)
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return 0

def guardar_resultats(ruta_fitxer, cadena, coincidencies):
    nom_fitxer = os.path.splitext(os.path.basename(ruta_fitxer))[0]
    with open(f"{nom_fitxer}_resultats.txt", "w") as f:
        f.write(f"Cadena de cerca: {cadena}\nCoincidències trobades: {coincidencies}\n")
