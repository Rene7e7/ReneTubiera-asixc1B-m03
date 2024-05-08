import funciones

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    palabra = input("Introduce la palabra a buscar: ")
    funciones.buscar_palabra(ruta_archivo, palabra)

if __name__ == "__main__":
    main()
