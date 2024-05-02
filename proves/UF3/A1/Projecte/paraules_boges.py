'''

Rene i Jordi

Per tant, les dades caldrà agafar-les d’un arxiu d’entrada. I la sortida, que generi el programa caldrà escriure-la en un altre arxiu de sortida. L’aplicació NO ha de tenir menú, l’execució es “desatesa” i els resultats, o estan a arxius de sortida o als de log.
Arxiu d’entrada: 	paraules.txt
Arxiu de sortida: 	paraules_boges.txt
Arxiu d’errors: 	boges.log

boges.log servirà per mostrar tota informació, error… relacionat amb el funcionament del programa. És a dir, informarà de quan s’ha iniciat el programa i quan ha acabat, a part dels errors / problemes trobats o qualsevol altra dada que es considera important.

'''

from datetime import datetime
# arxiu d’entrada: 	paraules.txt leer
# paraules.txt lee el fitxero i paraules_boges genera el fitxero donde las palabras estan desordenadas (aleatorizar part medio)
def llegir_arxiu():
    try:
        with open("paraules.txt", "r") as f:
            oracio = f.read()
    except FileNotFoundError:
        with open("boges.log", "w") as f:
            f.write(f"Fitxer/Directory no trobat: paraules.txt\n")
        print("Fitxer/Directory no trobat: paraules.txt")
    return oracio

try:
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

    # arxiu d’errors: 	boges.log
    with open("boges.log", "w") as f:
        f.write(f"Programa finalitzat: {datetime.now()}\n")

    # crida a les funcions
    paraules = dividir(oracio)
    paraules_desordenades = identificar_paraules(paraules)
    paraules_aleatoritzades = [aleatorizar_parte_medio(paraula) if paraula in paraules_desordenades else paraula for paraula
                               in paraules]
    juntar_llista(paraules_aleatoritzades)

except FileNotFoundError:
    with open("boges.log", "w") as f:
        f.write(f"Fitxer/Directory no trobat: paraules.txt\n")
    print("Fitxer/Directory no trobat: paraules.txt")
except Exception as e:
    with open("boges.log", "w") as f:
        f.write(f"Error: {e}\n")
    print(f"Error: {e}")
# arxiu de sortida: 	paraules_boges.txt
with open("paraules_boges.txt", "w") as f:
    f.write(juntar_llista(paraules_aleatoritzades))
