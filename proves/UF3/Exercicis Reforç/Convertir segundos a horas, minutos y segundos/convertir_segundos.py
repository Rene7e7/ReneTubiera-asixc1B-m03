import funciones_convertir_segundos as fcs

def main():
    segundos = int(input("Introduce la cantidad de segundos: "))
    tiempo = fcs.convertir_segundos(segundos)
    print(f"El tiempo es: {tiempo}")

if __name__ == "__main__":
    main()
