import random
import os
from log import escriure_log

# Lista de caracteres especiales
LISTA =  [".", ",", ";", ":", "?", "!"]

def llegir_arxiu(nom_arxiu):
    try:
        with open(nom_arxiu, "r") as f:
            oracio = f.readlines()
    except FileNotFoundError:
        escriure_log(f"Fitxer/Directory no trobat: {nom_arxiu}")
        print(f"Fitxer/Directory no trobat: {nom_arxiu}")
        oracio = []
    return oracio

def escriure_arxiu(nom_arxiu, llista):
    nom_sortida = nom_arxiu.replace("entrada", "sortida").replace(".txt", "_boges.txt")
    with open(nom_sortida, "w") as f:
        for paraula in llista:
            f.write(paraula + "\n")
    print(f"Fitxer {nom_sortida} creat correctament")

def dividir(oracio):
    paraules = []
    for linia in oracio:
        paraules += linia.split()
    return paraules

def identificar_paraules(paraules):
    paraules_desordenades = []
    for paraula in paraules:
        if len(paraula) > 3:
            paraules_desordenades.append(paraula)
    return paraules_desordenades

def identificar_caracters_especials(paraula):
    caracters_especials = []
    for i, lletra in enumerate(paraula):
        if not lletra.isalnum():
            caracters_especials.append((lletra, i))
    return caracters_especials

def aleatoritzar_parte_mitjana(oracio):
    paraules_desordenades = identificar_paraules(dividir(oracio))
    paraules_ordenades = dividir(oracio)
    paraules_aleatoritzades = []
    for paraula in paraules_ordenades:
        if paraula in paraules_desordenades:
            caracters_especials = identificar_caracters_especials(paraula)
            if caracters_especials:
                for caracter in caracters_especials:
                    paraula = paraula.replace(caracter[0], "")
                paraula = list(paraula)
                random.shuffle(paraula)
                for caracter in caracters_especials:
                    paraula.insert(caracter[1], caracter[0])
                paraula = "".join(paraula)
            else:
                paraula = list(paraula)
                random.shuffle(paraula)
                paraula = "".join(paraula)
        paraules_aleatoritzades.append(paraula)
    return paraules_aleatoritzades

def processar_arxiu(nom_arxiu, directori_log):
    oracio = llegir_arxiu(nom_arxiu)
    if oracio:
        paraules_aleatoritzades = aleatoritzar_parte_mitjana(oracio)
        # Comprova si les paraules de l'arxiu han canviat
        if paraules_aleatoritzades != dividir(oracio):
            escriure_arxiu(nom_arxiu, paraules_aleatoritzades)
        else:
            # Si les paraules no han canviat, escriu un missatge de WARNING al fitxer de log
            nom_arxiu = os.path.basename(nom_arxiu)
            escriure_log(f"WARNING: El fitxer {nom_arxiu} no ha estat processat i no ha estat modificat")
    else:
        escriure_log(f"Error al llegir l'arxiu {nom_arxiu}")
