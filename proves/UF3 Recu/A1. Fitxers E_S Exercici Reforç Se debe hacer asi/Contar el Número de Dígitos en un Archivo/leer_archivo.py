def leer_archivo(archivo_entrada):
    try:
        # Se abre el archivo en modo lectura y se lee su contenido
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            # Se retorna el contenido del archivo
            # no se usa readlines() porque no se necesita una lista con las líneas del archivo
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
