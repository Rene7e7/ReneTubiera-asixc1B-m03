def simular_llum(ruta_fitxer):
    llum_encesa = False
    with open(ruta_fitxer, "r") as f:
        for linia in f:
            accio = linia.strip()
            print(f">{accio}")
            if accio == "TURN ON":
                llum_encesa = True
            elif accio == "TURN OFF":
                llum_encesa = False
            elif accio == "TOGGLE":
                llum_encesa = not llum_encesa
            elif accio == "END":
                print("Fi del fitxer")
                break
            else:
                print("Acció no vàlida")
            print(llum_encesa)

    if accio != "END":
        print("Atenció: El fitxer no acaba amb l'acció 'END'")

