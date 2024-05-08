import gastos

def main():
    ruta_fitxer = "registre_gastos.txt"
    registre = gastos.llegir_gastos(ruta_fitxer)

    print("1. Afegir gasto")
    print("2. Calcular total de gastos")
    print("3. Guardar i sortir")
    opcio = input("Escull una opció: ")

    while opcio != "3":
        if opcio == "1":
            concepte = input("Concepte del gasto: ")
            importe = float(input("Import del gasto: "))
            gastos.afegir_gasto(registre, concepte, importe)
        elif opcio == "2":
            print(f"Total de gastos: {gastos.total_gastos(registre)}")
        opcio = input("Escull una opció: ")

    gastos.guardar_gastos(ruta_fitxer, registre)

if __name__ == "__main__":
    main()
