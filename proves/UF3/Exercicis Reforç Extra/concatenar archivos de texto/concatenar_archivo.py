import os
import funciones_concatenar as fc

def main():
    num_archivos = int(input("Introduce el número de archivos a concatenar: "))
    rutas_archivos = [input(f"Introduce la ruta del archivo {i+1}: ") for i in range(num_archivos)]
    ruta_archivo_nuevo = input("Introduce la ruta del nuevo archivo: ")
    fc.concatenar_archivos(rutas_archivos, ruta_archivo_nuevo)
    print("Archivos concatenados correctamente.")

if __name__ == "__main__":
    main()
