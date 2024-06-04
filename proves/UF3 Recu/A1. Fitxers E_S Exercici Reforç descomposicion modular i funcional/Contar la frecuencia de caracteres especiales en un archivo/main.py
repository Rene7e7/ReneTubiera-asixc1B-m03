from collections import Counter
import string

def contar_caracteres_especiales(contenido):
    # Definir caracteres especiales como cualquier cosa que no sea letra o número
    caracteres_especiales = set(string.punctuation + string.whitespace)

    # Contar la frecuencia de cada caracter especial
    contador = Counter(contenido)
    for char in contador:
        if char not in caracteres_especiales:
            del contador[char]

    return contador

def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for caracter, frecuencia in resultado.items():
                archivo.write(f'Caracter especial "{caracter}": {frecuencia} veces\n')
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

def procesar_archivo(archivo_entrada, archivo_salida):
    contenido = leer_archivo(archivo_entrada)
    if contenido is not None:
        contador = contar_caracteres_especiales(contenido)
        escribir_resultado(archivo_salida, contador)
        return contador
    return None

if __name__ == "__main__":
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_caracteres_especiales.txt'
    contador = procesar_archivo(archivo_entrada, archivo_salida)
    print(f"El resultado se ha guardado en {archivo_salida}.")
