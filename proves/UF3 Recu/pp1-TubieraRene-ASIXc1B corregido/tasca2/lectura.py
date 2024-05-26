def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return []
