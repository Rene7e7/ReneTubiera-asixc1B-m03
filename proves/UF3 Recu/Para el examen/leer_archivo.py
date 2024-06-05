def leer_archivo(archivo_entrada):
    """Lee el contenido de un archivo y devuelve las líneas como una lista."""
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        return lineas
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return []
