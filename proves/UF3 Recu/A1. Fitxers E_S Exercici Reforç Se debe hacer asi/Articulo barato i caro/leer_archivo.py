def leer_datos(archivo_entrada):
    try:
        # Leer los datos del archivo y devolverlos como una lista de listas
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            # Leer las líneas del archivo y dividirlas por el punto y coma
            datos = [linea.strip().split(';') for linea in archivo.readlines()]
            # Convertir los precios a números decimales
            return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None
