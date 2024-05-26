import funciones_generar_numeros as fgn

def main():
    cantidad_numeros = int(input("Introduce la cantidad de números aleatorios: "))
    minimo = int(input("Introduce el valor mínimo: "))
    maximo = int(input("Introduce el valor máximo: "))
    fgn.generar_numeros_aleatorios(cantidad_numeros, minimo, maximo)
    print("Números aleatorios generados correctamente.")

if __name__ == "__main__":
    main()
