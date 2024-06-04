def leer_lineas(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
            return entrada.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return []
