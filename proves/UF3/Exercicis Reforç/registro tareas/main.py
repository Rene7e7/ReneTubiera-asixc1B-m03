import tareas

def main():
    ruta_fitxer = "llista_tasques.txt"
    registre = tareas.llegir_tasques(ruta_fitxer)

    print("1. Afegir tasca")
    print("2. Marcar tasca completada")
    print("3. Guardar i sortir")
    opcio = input("Escull una opció: ")

    while opcio != "3":
        if opcio == "1":
            tasca = input("Nova tasca: ")
            tareas.afegir_tasca(registre, tasca)
        elif opcio == "2":
            index = int(input("Índex de la tasca a marcar com a completada: "))
            tareas.marcar_completada(registre, index)
        opcio = input("Escull una opció: ")

    tareas.guardar_tasques(ruta_fitxer, registre)

if __name__ == "__main__":
    main()
