'''
Aquesta versió haurà de processar tots els arxius, amb extensió txt del directori d'entrada.
Haurà de generar un fitxer de sortida per a cada un dels que trobi a l’entrada amb el mateix nom, afegint “_boges”. I evidentment, processat ;-)
Exemple: paraules.txt → paraules_boges.txt

Directoris de treball
Directori d’entrada: 		./entrada
Directori de sortida: 		./sortida
Directori de log: 		    ./log
'''
import random

# Llista dels caracters especials
LISTA =  [".", ",", ";", ":", "?", "!"]

def llegir_arxiu():
    try:
        with open("paraules.txt", "r") as f:
            oracio = f.readlines()
    except FileNotFoundError:
        with open("boges.log", "a") as f:
            f.write(f"Fitxer/Directory no trobat: paraules.txt\n")
        print("Fitxer/Directory no trobat: paraules.txt")
        oracio = []
    return oracio

def escriure_arxiu(llista):
    with open("paraules_boges.txt", "w") as f:
        for paraula in llista:
            f.write(paraula + "\n")


def escriure_log(missatge):
    with open("boges.log", "a") as f:
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

def main():
    oracio = llegir_arxiu()
    if oracio:
        paraules = dividir(oracio)
        paraules_desordenades = identificar_paraules(paraules)
        paraules_aleatoritzades = [aleatoritzar_parte_mitjana(paraula) if paraula in paraules_desordenades else paraula for paraula in paraules]
        escriure_arxiu(paraules_aleatoritzades)
        escriure_log("Inici del programa")
        escriure_log("Final del programa")
    else:
        escriure_log("Inici del programa sense fitxer d'entrada")
        escriure_log("Final del programa sense fitxer d'entrada")

if __name__ == "__main__":
    main()
