import contador

def main():
    ruta_fitxer = input("Introdueix la ruta del fitxer: ")
    linies, paraules, caracters = contador.contar(ruta_fitxer)
    contador.guardar_resultats(ruta_fitxer, linies, paraules, caracters)
    print("Resultats guardats correctament.")

if __name__ == "__main__":
    main()
