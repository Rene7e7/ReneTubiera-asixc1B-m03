from preus import llegir_preus, preu_mes_baix

def main():
    ruta_fitxer = input("Introdueix la ruta al fitxer: ")
    preus = llegir_preus(ruta_fitxer)
    preu_minim = preu_mes_baix(preus)
    print(f"El producte més econòmic val: {preu_minim}€")

if __name__ == "__main__":
    main()
