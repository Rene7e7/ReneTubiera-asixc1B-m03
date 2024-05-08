import os
import funciones_buscar_palabra as fbp

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    palabra_buscar = input("Palabra a buscar: ")
    fbp.buscar_palabra(ruta_archivo, palabra_buscar)

if __name__ == "__main__":
    main()
