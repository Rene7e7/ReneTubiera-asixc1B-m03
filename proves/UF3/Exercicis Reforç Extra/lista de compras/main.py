import compras

def main():
    ruta_fitxer = "llista_compres.txt"
    registre = compras.llegir_compres(ruta_fitxer)

    print("1. Afegir producte")
    print("2. Marcar producte com comprat")
    print("3. Guardar i sortir")
    opcio = input("Escull una opció: ")

    while opcio != "3":
        if opcio == "1":
            producte = input("Nou producte: ")
            compras.afegir_producte(registre, producte)
        elif opcio == "2":
            index = int(input("Índex del producte a marcar com a comprat: "))
            compras.marcar_comprat(registre, index)
        opcio = input("Escull una opció: ")

    compras.guardar_compres(ruta_fitxer, registre)

if __name__ == "__main__":
    main()
