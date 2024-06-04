def leer_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
        return None
