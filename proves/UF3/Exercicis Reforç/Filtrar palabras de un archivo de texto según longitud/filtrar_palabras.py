import funciones_filtrar_palabras as ffp

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    longitud = int(input("Introduce la longitud de las palabras a filtrar: "))
    ffp.filtrar_palabras(ruta_archivo, longitud)
    print("Palabras filtradas correctamente.")

if __name__ == "__main__":
    main()
