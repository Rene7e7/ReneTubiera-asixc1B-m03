import procesar_archivo

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'paraules.txt'
    # Nombre del archivo para palabras que terminan en 'ción'
    archivo_terminaciones = 'terminaciones.txt'
    # Nombre del archivo para otras palabras
    archivo_otras = 'otras.txt'

    # Llamar a la función para procesar el archivo
    procesar_archivo.procesar_archivo(archivo_entrada, archivo_terminaciones, archivo_otras)

    print("Proceso completado. Las palabras se han filtrado y guardado correctamente.")

if __name__ == "__main__":
    main()
