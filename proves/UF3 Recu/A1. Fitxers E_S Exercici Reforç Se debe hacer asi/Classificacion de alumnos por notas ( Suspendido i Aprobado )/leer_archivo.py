def leer_archivo(archivo_entrada):
    try:
        # Abrir el archivo en modo lectura
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            # Devolver el contenido del archivo como una lista de líneas
            # readlines lo que hace es leer el archivo línea por línea y devolver una lista con las líneas
            return archivo.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
