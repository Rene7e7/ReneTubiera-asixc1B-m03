import calculadora

def main():
    ruta_fitxer = "historial_operacions.txt"
    historial = calculadora.llegir_historial(ruta_fitxer)

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Guardar i sortir")
    opcio = input("Escull una opció: ")

    while opcio != "5":
        if opcio in ["1", "2", "3", "4"]:
            a = float(input("Primer nombre: "))
            b = float(input("Segon nombre: "))
            if opcio == "1":
                resultat = calculadora.suma(a, b)
            elif opcio == "2":
                resultat = calculadora.resta(a, b)
            elif opcio == "3":
                resultat = calculadora.multiplicacio(a, b)
            elif opcio == "4":
                resultat = calculadora.divisio(a, b)
            print(f"Resultat: {resultat}")
            historial.append(f"{a} + {b} = {resultat}")
        opcio = input("Escull una opció: ")

    calculadora.guardar_historial(ruta_fitxer, historial)

if __name__ == "__main__":
    main()
