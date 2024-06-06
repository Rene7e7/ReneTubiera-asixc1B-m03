# leer_archivo.py
def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read().split()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{ruta_archivo}': {e}")
        return []
