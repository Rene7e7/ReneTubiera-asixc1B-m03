import funciones

def main():
    archivo1 = input("Introduce la ruta del primer archivo: ")
    archivo2 = input("Introduce la ruta del segundo archivo: ")
    archivo_combinado = input("Introduce la ruta del archivo combinado: ")
    funciones.combinar_archivos(archivo1, archivo2, archivo_combinado)

if __name__ == "__main__":
    main()
