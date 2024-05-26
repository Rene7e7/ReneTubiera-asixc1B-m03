import fitxer

def analitzar_partit(ruta_fitxer):
    resultats = fitxer.llegir_fitxer(ruta_fitxer)

    for equip, accio in resultats:
        if accio == 1:
            print(f"Cistella de {equip}")
        elif accio == 2:
            print(f"Doble de {equip}")
        elif accio == 3:
            print(f"Triple de {equip}")
        else:
            print(f"Tir lliure de {equip}")
