import empleados

def main():
    ruta_fitxer = "empleats.txt"
    registre = empleados.llegir_empleats(ruta_fitxer)

    print("1. Afegir empleat")
    print("2. Buscar empleat")
    print("3. Guardar i sortir")
    opcio = input("Escull una opció: ")

    while opcio != "3":
        if opcio == "1":
            nom = input("Nom del empleat: ")
            cognoms = input("Cognoms del empleat: ")
            departament = input("Departament del empleat: ")
            empleados.afegir_empleat(registre, nom, cognoms, departament)
        elif opcio == "2":
            nom = input("Nom del empleat a buscar: ")
            resultats = empleados.buscar_empleat(registre, nom)
            if resultats:
                print("Empleats trobats:")
                for empleat in resultats:
                    print(f"Nom: {empleat['nom']}, Cognoms: {empleat['cognoms']}, Departament: {empleat['departament']}")
            else:
                print("No s'ha trobat cap empleat amb aquest nom.")
        opcio = input("Escull una opció: ")

    empleados.guardar_empleats(ruta_fitxer, registre)

if __name__ == "__main__":
    main()
