from collections import Counter
import re

def contar_vocales(contenido):
    # Validar que el contenido no esté vacío
    if not contenido.strip():
        print("El archivo está vacío o solo contiene espacios en blanco.")
        return None

    # Usar una expresión regular para separar las vocales de manera más precisa
    vocales = re.findall(r'[aeiouAEIOU]', contenido)

    # Contar la frecuencia de cada vocal
    contador = Counter(vocales)

    return contador

def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for vocal, frecuencia in resultado.items():
                archivo.write(f'Vocal "{vocal}": {frecuencia} veces\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")

def leer_archivo(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None

# Asegúrate de que las funciones estén definidas aquí o importadas correctamente
if __name__ == "__main__":
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_vocales.txt'
    contenido = leer_archivo(archivo_entrada)
    if contenido is not None:
        contador = contar_vocales(contenido)
        if contador is not None:
            escribir_resultado(archivo_salida, contador)
