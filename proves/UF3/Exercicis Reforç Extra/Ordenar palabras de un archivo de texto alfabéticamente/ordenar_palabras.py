import os
import funciones_ordenar_palabras as fop

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    fop.ordenar_palabras(ruta_archivo)
    print("Palabras ordenadas correctamente.")

if __name__ == "__main__":
    main()
