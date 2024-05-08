import analizador

def main():
    ruta_fitxer = input("Introdueix la ruta del fitxer de log: ")
    cadena = input("Introdueix la cadena a buscar: ")
    coincidencies = analizador.analitzar_log(ruta_fitxer, cadena)
    analizador.guardar_resultats(ruta_fitxer, cadena, coincidencies)
    print("Resultats guardats correctament.")

if __name__ == "__main__":
    main()
