import funciones_comprobar_archivo_vacio as fcv

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    if fcv.archivo_vacio(ruta_archivo):
        print("El archivo está vacío.")
    else:
        print("El archivo no está vacío.")

if __name__ == "__main__":
    main()
