import re
from collections import Counter

def contar_numeros(contenido):
    # Usamos una expresión regular para encontrar todos los números
    numeros_encontrados = re.findall(r'\b\d+\b', contenido)
    numeros_enteros = [int(num) for num in numeros_encontrados]

    # Contar la frecuencia de cada número
    contador = Counter(numeros_enteros)

    return contador

def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for numero, frecuencia in resultado.items():
                archivo.write(f'Número {numero}: {frecuencia} veces\n')
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
        contador = contar_numeros(contenido)
        escribir_resultado(archivo_salida, contador)
        return contador
    return None

if __name__ == "__main__":
    archivo_entrada = 'numeros.txt'
    archivo_salida = 'resultado_numeros.txt'
    contador = procesar_archivo(archivo_entrada, archivo_salida)
    print(f"El resultado se ha guardado en {archivo_salida}.")
