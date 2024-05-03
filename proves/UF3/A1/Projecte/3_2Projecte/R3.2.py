'''
Aquesta versió haurà de processar tots els arxius, amb extensió txt del directori d'entrada.
Haurà de generar un fitxer de sortida per a cada un dels que trobi a l’entrada amb el mateix nom, afegint “_boges”. I evidentment, processat ;-)
Exemple: paraules.txt → paraules_boges.txt

Directoris de treball
Directori d’entrada: 		./entrada
Directori de sortida: 		./sortida
Directori de log: 		    ./log
'''
import os
import random

# Lista de caracteres especiales
LISTA =  [".", ",", ";", ":", "?", "!"]

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

def escriure_arxiu(nom_arxiu, llista):
    nom_sortida = nom_arxiu.replace("entrada", "sortida").replace(".txt", "_boges.txt")
    with open(nom_sortida, "w") as f:
        for paraula in llista:
            f.write(paraula + "\n")

def escriure_log(missatge):
    with open("log/boges.log", "a") as f:
        f.write(missatge + "\n")

def dividir(oracio):
    paraules = []
    for linia in oracio:
        paraules += linia.split()
    return paraules

def identificar_paraules(paraules):
    paraules_desordenades = []
    for paraula in paraules:
        # Comprova si te mes de 3 lletras per fer el randomitzador
        if len(paraula) > 3:
            paraules_desordenades.append(paraula)
    return paraules_desordenades

def identificar_caracters_especials(paraula):
    caracters_especials = []
    for i, lletra in enumerate(paraula):
        # Comanda isalnum son tots el caractes que no siguin caracters especials
        if not lletra.isalnum():
            caracters_especials.append((lletra, i))
    return caracters_especials

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

def juntar_llista(llista):
    return [paraula + "\n" for paraula in llista]

def processar_arxiu(nom_arxiu):
    oracio = llegir_arxiu(nom_arxiu)
    if oracio:
        paraules = dividir(oracio)
        paraules_desordenades = identificar_paraules(paraules)
        paraules_aleatoritzades = [aleatoritzar_parte_mitjana(paraula) if paraula in paraules_desordenades else paraula for paraula in paraules]
        escriure_arxiu(nom_arxiu, paraules_aleatoritzades)
        escriure_log(f"Processat correctament: {nom_arxiu}")
    else:
        escriure_log(f"Error en processar: {nom_arxiu}")

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

if __name__ == "__main__":
    main()

