def leer_archivo(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo}': {e}")
        return None
