import os
import funciones_contador as fc

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    palabras = fc.contar_palabras(ruta_archivo)
    print(f"El archivo tiene {palabras} palabras.")

if __name__ == "__main__":
    main()
