import re

def contar_palabras(texto):
    # Validar que el contenido no esté vacío
    if not texto.strip():
        print("El archivo está vacío o solo contiene espacios en blanco.")
        return None

    # Usar una expresión regular para separar las palabras de manera más precisa
    palabras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', texto)
    frecuencia_palabras = {}
    for palabra in palabras:
        palabra = palabra.lower()
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    return frecuencia_palabras

def contar_numeros(texto):
    # Usar una expresión regular para separar los números de manera más precisa
    numeros = re.findall(r'\b\d+\b', texto)
    frecuencia_numeros = {}
    for numero in numeros:
        frecuencia_numeros[numero] = frecuencia_numeros.get(numero, 0) + 1
    return frecuencia_numeros

def escribir_resultados(archivo_salida, datos, tipo):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for elemento, frecuencia in datos.items():
                archivo.write(f'{elemento}: {frecuencia}\n')
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
    texto = leer_archivo('texto.txt')
    if texto:
        frecuencia_palabras = contar_palabras(texto)
        frecuencia_numeros = contar_numeros(texto)

        escribir_resultados('frecuencia_palabras.txt', frecuencia_palabras, 'palabras')
        escribir_resultados('frecuencia_numeros.txt', frecuencia_numeros, 'números')
