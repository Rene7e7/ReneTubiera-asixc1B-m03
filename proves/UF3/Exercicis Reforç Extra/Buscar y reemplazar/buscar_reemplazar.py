import os
import funciones_buscar_reemplazar as fbr

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    palabra_buscar = input("Palabra a buscar: ")
    palabra_reemplazar = input("Palabra de reemplazo: ")
    fbr.buscar_reemplazar(ruta_archivo, palabra_buscar, palabra_reemplazar)

if __name__ == "__main__":
    main()
