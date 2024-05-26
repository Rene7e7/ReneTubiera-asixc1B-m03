import estudiante

def main():
    ruta_fitxer = "registre_estudiants.txt"
    registre = estudiante.llegir_registre(ruta_fitxer)

    print("1. Afegir estudiant")
    print("2. Buscar estudiant")
    print("3. Guardar i sortir")
    opcio = input("Escull una opció: ")

    while opcio != "3":
        if opcio == "1":
            nom = input("Nom de l'estudiant: ")
            edat = int(input("Edat de l'estudiant: "))
            estudiante.afegir_estudiant(registre, nom, edat)
        elif opcio == "2":
            nom = input("Nom de l'estudiant a buscar: ")
            estudiant = estudiante.buscar_estudiant(registre, nom)
            if estudiant:
                print(f"Estudiant trobat: {estudiant['nom']}, {estudiant['edat']} anys")
            else:
                print("Estudiant no trobat")
        opcio = input("Escull una opció: ")

    estudiante.guardar_registre(ruta_fitxer, registre)

if __name__ == "__main__":
    main()
