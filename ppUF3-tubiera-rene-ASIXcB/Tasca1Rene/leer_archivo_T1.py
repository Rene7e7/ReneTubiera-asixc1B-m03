def leer_archivo(ruta_archivo):
    try:
        # Obre el fitxer en mode lectura
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Retorna el arxiu llegit
            return archivo.read().split()
    # si no es troba el fitxer mostra un missatge de error que no s'ha trobat el arxiu
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return []
    # Dona un altre error de arxiu
    except Exception as e:
        print(f"Error al leer el archivo '{ruta_archivo}': {e}")
        return []

