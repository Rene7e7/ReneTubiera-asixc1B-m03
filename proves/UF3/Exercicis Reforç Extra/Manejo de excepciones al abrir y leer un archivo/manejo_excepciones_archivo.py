import funciones_manejo_excepciones_archivo as fmea

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    fmea.leer_archivo(ruta_archivo)

if __name__ == "__main__":
    main()
