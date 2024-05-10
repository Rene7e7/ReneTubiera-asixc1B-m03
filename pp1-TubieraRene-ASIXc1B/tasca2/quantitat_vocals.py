'''
Rene Tubiera Sadinas
M03 UF3 A1
9/5/2024
pp1-Tubiera-Rene-ASIXc1B
'''
def separar_llista_lletres(ruta_archivo):
    lletres = "paraules.txt"
    # Separa les lletres en una llista
    llista_lletres = lletres.split()

    # Inicialitza una llista buida per emmagatzemar les vocals
    vocals = []

    with open("ParaulesQuantitatVocals.txt", "r") as f:
        # Itera sobre cada lletra i comprova si és una vocal
        for lletra in ruta_archivo:
            # tambe transforma les vocals que estan en majuscules en minuscules
            if lletra.lower() in ['a', 'e', 'i', 'o', 'u']:
                vocals.append(llista_lletres)
                quantitat_vocals = len(lletra)
                return lletra




