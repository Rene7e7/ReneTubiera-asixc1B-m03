'''
En aquest lliurament cal aprofitar tota la feina feta fins ara, és a dir el 1r i 2n lliurament i afegir el tractament de fitxers.
Per tant, les dades caldrà agafar-les d’un arxiu d’entrada. I la sortida, que generi el programa caldrà escriure-la en un altre arxiu de sortida. L’aplicació NO ha de tenir menú, l’execució es “desatesa” i els resultats, o estan a arxius de sortida o als de log.
Arxiu d’entrada: 	paraules.txt
Arxiu de sortida: 	paraules_boges.txt
Arxiu d’errors: 	boges.log

boges.log servirà per mostrar tota informació, error… relacionat amb el funcionament del programa. És a dir, informarà de quan s’ha iniciat el programa i quan ha acabat, a part dels errors / problemes trobats o qualsevol altra dada que es considera important.

Aquest arxiu log, no es podrà sobreescriure, haurà d’acumular un “històric” de tota la informació de les diferents execucions del programa

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
        for linia in llista:
            f.write(" ".join(linia) + "\n")

def escriure_log(missatge):
    with open("boges.log", "a") as f:
        f.write(missatge + "\n")

def dividir(oracio):
    paraules = []
    for linia in oracio:
        paraules.append(linia.split())
    return paraules

def identificar_paraules(paraules):
    paraules_desordenades = []
    for linia in paraules:
        for paraula in linia:
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
    return [[aleatoritzar_parte_mitjana(paraula) if len(paraula) > 3 else paraula for paraula in linia] for linia in llista]

def main():
    oracio = llegir_arxiu()
    if oracio:
        paraules = dividir(oracio)
        paraules_desordenades = identificar_paraules(paraules)
        paraules_aleatoritzades = juntar_llista(paraules)
        escriure_arxiu(paraules_aleatoritzades)
        escriure_log("Inici del programa")
        escriure_log("Final del programa")
    else:
        escriure_log("Inici del programa sense fitxer d'entrada")
        escriure_log("Final del programa sense fitxer d'entrada")

if __name__ == "__main__":
    main()
