def leer_archivo(archivo_entrada):
    try:
        # Lee el contenido del archivo y lo devuelve como una cadena de texto.
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            # Devolver el contenido del archivo
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
