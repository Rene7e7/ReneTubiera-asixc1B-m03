import random
# Llista dels caracters especials
LISTA =  [".", ",", ";", ":", "?", "!"]
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
    print(frase)
    return frase
# crida a les funcions
oracio = input("Introduce una oracion: ")
paraules = dividir(oracio)
paraules_desordenades = identificar_paraules(paraules)
paraules_aleatoritzades = [aleatorizar_parte_medio(paraula) if paraula in paraules_desordenades else paraula for paraula
                           in paraules]
juntar_llista(paraules_aleatoritzades)