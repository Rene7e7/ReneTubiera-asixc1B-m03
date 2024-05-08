def llegir_preus(ruta_fitxer):
    with open(ruta_fitxer, "r") as f:
        linia = f.readline().strip()
        preus = [int(x) for x in linia.split()]
    return preus

def preu_mes_baix(preus):
    preu_minim = preus[0]
    for preu in preus:
        if preu < preu_minim:
            preu_minim = preu
    return preu_minim
