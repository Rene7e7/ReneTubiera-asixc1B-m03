def leer_datos(archivo_entrada):
    try:
        # Leer los datos del archivo y devolverlos como una lista de cadenas
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            # Leer las líneas del archivo y devolverlas como una lista de cadenas
            datos = [linea.strip() for linea in archivo.readlines()]
            # Devolver los datos
            return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
