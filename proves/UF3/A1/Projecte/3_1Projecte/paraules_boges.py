# region Importacions
import random
import os
from log import escriure_log
# endregion
# region Llista dels caracters especials
LISTA =  [".", ",", ";", ":", "?", "!"]
# endregion
# region llegir_arxiu
def llegir_arxiu():
    oracio = []
    try:
        with open("paraules.txt", "r") as f:
            for linia in f:
                oracio.append(linia)
    except FileNotFoundError:
        escriure_log(f"Fitxer/Directory no trobat: paraules.txt")
        print("Fitxer/Directory no trobat: paraules.txt")
    return oracio
# endregion
# region escriure_arxiu
def escriure_arxiu(llista):
    with open("paraules_boges.txt", "w") as f:
        for paraula in llista:
            f.write(paraula + "\n")
# endregion
# region dividir
def dividir(oracio):
    paraules = []
    for linia in oracio:
        paraules += linia.split()
    return paraules
# endregion
# region identificar_paraules

def identificar_paraules(paraules):
    paraules_desordenades = []
    for paraula in paraules:
        # Comprova si te mes de 3 lletras per fer el randomitzador
        if len(paraula) > 3:
            paraules_desordenades.append(paraula)
    return paraules_desordenades
# endregion
# region identificar_caracters_especials
def identificar_caracters_especials(paraula):
    caracters_especials = []
    for i, lletra in enumerate(paraula):
        # Comanda isalnum son tots el caractes que no siguin caracters especials
        if not lletra.isalnum():
            caracters_especials.append((lletra, i))
    return caracters_especials
# endregion
# region aleatoritzar_parte_mitjana
def aleatoritzar_parte_mitjana(oracio):
    paraules_desordenades = identificar_paraules(dividir(oracio))
    paraules_ordenades = dividir(oracio)
    paraules_aleatoritzades = []

    for paraula in paraules_ordenades:
        if paraula in paraules_desordenades:
            paraules_desordenades.remove(paraula)
            caracters_especials = identificar_caracters_especials(paraula)
            part_inicial = paraula[0]
            part_final = paraula[-1]
            medio = list(paraula[1:-1])
            # Fa una neteja de quitant i guardan totes les posicions dels caracters especials
            part_media = [char for char in medio if char.isalnum()]
            if len(medio) > len(part_media):
                ultima_part_media = part_media[-1]
                part_media = part_media[:-1]
                random.shuffle(part_media)
                part_media.append(ultima_part_media)
            else:
                random.shuffle(part_media)
            for character in paraula:
                # Aqui fa una comprovacio de numeros amb caracters especials
                if character.isdigit():
                    paraules_aleatoritzades.append(part_inicial + "".join(medio) + part_final)
            for char, pos in caracters_especials:
                part_media.insert(pos - 1, char)
            if part_final in LISTA:
                # Unio de les parts
                paraules_aleatoritzades.append(part_inicial + "".join(part_media))
            else:
                paraules_aleatoritzades.append(part_inicial + "".join(part_media) + part_final)
        else:
            paraules_aleatoritzades.append(paraula)

    return paraules_aleatoritzades
# endregion