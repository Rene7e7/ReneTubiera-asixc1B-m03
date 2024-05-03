'''
Rene i Jordi
Aquesta versió haurà de mostrar el temps transcorregut en processar els arxius.

'''
# region Imports
import os
import random
import time
# endregion
# region Lista de caracteres especiales
LISTA =  [".", ",", ";", ":", "?", "!"]
# endregion
# region llegir_arxiu
def llegir_arxiu(nom_arxiu):
    try:
        with open(nom_arxiu, "r") as f:
            oracio = f.readlines()
    except FileNotFoundError:
        with open("log/boges.log", "a") as f:
            f.write(f"Fitxer/Directory no trobat: {nom_arxiu}\n")
        print(f"Fitxer/Directory no trobat: {nom_arxiu}")
        oracio = []
    return oracio
# endregion
# region escriure_arxiu
def escriure_arxiu(nom_arxiu, llista):
    nom_sortida = nom_arxiu.replace("entrada", "sortida").replace(".txt", "_boges.txt")
    with open(nom_sortida, "w") as f:
        for paraula in llista:
            f.write(paraula + "\n")
# endregion
# region escriure_log
def escriure_log(missatge):
    with open("log/boges.log", "a") as f:
        f.write(missatge + "\n")
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
# region identificar_paraules_especials
def identificar_caracters_especials(paraula):
    caracters_especials = []
    for i, lletra in enumerate(paraula):
        # Comanda isalnum son tots el caractes que no siguin caracters especials
        if not lletra.isalnum():
            caracters_especials.append((lletra, i))
    return caracters_especials
# endregion
# region aleatoritzar_parte_mitjana
def aleatoritzar_parte_mitjana(paraula):
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
            return part_inicial + "".join(medio) + part_final
    for char, pos in caracters_especials:
        part_media.insert(pos - 1, char)
    if part_final in LISTA:
        # Unio de les parts
        return part_inicial + "".join(part_media)
    else:
        return part_inicial + "".join(part_media) + part_final
# endregion
# region junta_llista
def juntar_llista(llista):
    return [paraula + "\n" for paraula in llista]
# endregion
# region processar_arxiu
def processar_arxiu(nom_arxiu):
    start_time = time.time()
    oracio = llegir_arxiu(nom_arxiu)
    if oracio:
        paraules = dividir(oracio)
        paraules_desordenades = identificar_paraules(paraules)
        paraules_aleatoritzades = [aleatoritzar_parte_mitjana(paraula) if paraula in paraules_desordenades else paraula for paraula in paraules]
        escriure_arxiu(nom_arxiu, paraules_aleatoritzades)
        escriure_log(f"Processat correctament: {nom_arxiu}")
    else:
        escriure_log(f"Error en processar: {nom_arxiu}")
    elapsed_time = time.time() - start_time
    # lo que falta es mostrar el tiempo transcurrido en procesar los archivos
    # elapsed_time lo que fa es calcular el temps que ha trigat en processar el arxiu
    escriure_log(f"Temps transcorregut en processar {nom_arxiu}: {elapsed_time} segons")
# endregion
# region main
def main():
    directori_entrada = "./entrada"
    directori_sortida = "./sortida"
    directori_log = "./log"

    # Comprovar si els directoris de sortida i log existeixen, si no, crear-los
    for directori in [directori_entrada, directori_sortida, directori_log]:
        if not os.path.exists(directori):
            os.makedirs(directori)

    # Processar tots els arxius amb extensió .txt del directori d'entrada
    arxius_entrada = [f for f in os.listdir(directori_entrada) if f.endswith(".txt")]
    for arxiu in arxius_entrada:
        nom_arxiu = os.path.join(directori_entrada, arxiu)
        processar_arxiu(nom_arxiu)
# endregion
# region __main__
if __name__ == "__main__":
    main()
# endregion