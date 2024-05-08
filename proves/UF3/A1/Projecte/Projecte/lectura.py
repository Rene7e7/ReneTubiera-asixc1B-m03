from datetime import datetime
import os
from log import escriure_log

def llegir_arxiu():
    oracio = []
    try:
        with open("paraules.txt", "r") as f:
            for linia in f:
                oracio.append(linia.strip())
    except FileNotFoundError:
        escriure_log(f"Fitxer/Directory no trobat: paraules.txt")
        print("Fitxer/Directory no trobat: paraules.txt")
    return oracio
# endregion
# region escriure_arxiu
def escriure_arxiu(llista):
    with open("paraules_boges.txt", "w") as f:
        # Escriu les paraules en el fitxer en la misma posiion que estava
        for paraula in llista:
            f.write(paraula + "\n")
    print("Fitxer paraules_boges.txt creat correctament")