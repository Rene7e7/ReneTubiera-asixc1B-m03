import os
import random

# Llista dels caracters especials
LISTA = [".", ",", ";", ":", "?", "!"]

def dividir(oracio):
    paraules = oracio.split()
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

def aleatorizar_parte_medio(paraula):
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
            return part_inicial + "".join(paraula[1:-1]) + part_final
    for char, pos in caracters_especials:
        part_media.insert(pos - 1, char)
    if part_final in LISTA:
        # Unio de les parts
        return part_inicial + "".join(part_media)
    else:
        return part_inicial + "".join(part_media) + part_final

def juntar_llista(llista):
    frase = " ".join(llista)
    return frase

def processar_arxiu(entrada, sortida):
    with open(entrada, 'r') as file:
        contingut = file.read()
        paraules = dividir(contingut)
        paraules_desordenades = identificar_paraules(paraules)
        paraules_aleatoritzades = [aleatorizar_parte_medio(paraula) if paraula in paraules_desordenades else paraula
                                   for paraula in paraules]
        frase = juntar_llista(paraules_aleatoritzades)

    # Escriu el contingut processat al fitxer de sortida
    with open(sortida, 'w') as file:
        file.write(frase)

def processar_directori_entrada(entrada, sortida):
    if not os.path.exists(sortida):
        os.makedirs(sortida)

    arxius = [arxiu for arxiu in os.listdir(entrada) if arxiu.endswith('.txt')]
    for arxiu in arxius:
        arxiu_entrada = os.path.join(entrada, arxiu)
        arxiu_sortida = os.path.join(sortida, arxiu.replace('.txt', '_boges.txt'))
        processar_arxiu(arxiu_entrada, arxiu_sortida)

if __name__ == "__main__":
    directori_entrada = "./entrada"
    directori_sortida = "./sortida"
    processar_directori_entrada(directori_entrada, directori_sortida)
