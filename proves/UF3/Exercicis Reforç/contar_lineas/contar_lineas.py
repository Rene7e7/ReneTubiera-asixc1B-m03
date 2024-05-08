import os
import funciones_contar_lineas as fcl

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    lineas = fcl.contar_lineas(ruta_archivo)
    print(f"El archivo tiene {lineas} líneas.")

if __name__ == "__main__":
    main()
