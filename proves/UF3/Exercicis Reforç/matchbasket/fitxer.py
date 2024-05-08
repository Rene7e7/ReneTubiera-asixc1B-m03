def llegir_fitxer(ruta_fitxer):
    resultats = []
    with open(ruta_fitxer, "r") as f:
        linies = f.readlines()
        equip1 = linies[0].strip()
        equip2 = linies[1].strip()
        for linia in linies[2:]:
            accio = linia.strip().split()
            punts_equip1 = int(accio[0])
            punts_equip2 = int(accio[1])
            if punts_equip1 > punts_equip2:
                resultats.append((equip1, punts_equip1))
                resultats.append((equip2, punts_equip2))
            else:
                resultats.append((equip2, punts_equip2))
                resultats.append((equip1, punts_equip1))
    return resultats
