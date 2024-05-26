def leer_archivo(archivo):
    try:
        with open(archivo, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return []
