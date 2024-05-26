def leer_archivo(archivo_entrada):
    try:
        with open(archivo_entrada, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
