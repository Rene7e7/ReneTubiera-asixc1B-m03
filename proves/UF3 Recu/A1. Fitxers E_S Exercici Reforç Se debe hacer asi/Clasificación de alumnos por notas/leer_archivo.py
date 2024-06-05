def leer_archivo(archivo_entrada):
    try:
        # Lo que hace es abrir el archivo en modo lectura y codificación utf-8
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            # y devuelve el contenido del archivo como una cadena de texto
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
