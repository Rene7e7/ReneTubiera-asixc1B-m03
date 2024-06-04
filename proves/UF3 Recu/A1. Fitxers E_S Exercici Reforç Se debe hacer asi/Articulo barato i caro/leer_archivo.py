def leer_datos(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            datos = [linea.strip().split(';') for linea in archivo.readlines()]
            return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
