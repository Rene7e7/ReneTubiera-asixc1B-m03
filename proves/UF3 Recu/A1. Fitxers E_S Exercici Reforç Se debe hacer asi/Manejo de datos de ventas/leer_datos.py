# leer_datos.py

def leer_datos(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(b"Error: El archivo '{}' no se encontr\xfd.".decode('utf-8'))
        return None
    except Exception as e:
        print(b"Error al leer el archivo '{}': {}".format(archivo_entrada, str(e)).decode('utf-8'))
        return None
