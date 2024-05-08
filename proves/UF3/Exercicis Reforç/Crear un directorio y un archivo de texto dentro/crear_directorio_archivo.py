import os
import funciones_crear_directorio_archivo as fcda

def main():
    nombre_directorio = input("Introduce el nombre del directorio: ")
    nombre_archivo = input("Introduce el nombre del archivo: ")
    contenido_archivo = input("Introduce el contenido del archivo: ")
    fcda.crear_directorio_archivo(nombre_directorio, nombre_archivo, contenido_archivo)
    print("Directorio y archivo creados correctamente.")

if __name__ == "__main__":
    main()
