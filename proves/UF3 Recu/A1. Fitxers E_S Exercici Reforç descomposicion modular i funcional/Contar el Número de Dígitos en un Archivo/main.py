import re

def contar_digitos(texto):
    # Usamos una expresión regular para encontrar todos los dígitos
    digitos_encontrados = re.findall(r'\d', texto)
    return len(digitos_encontrados)

def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(f"El archivo contiene {resultado} dígitos.\n")
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
    texto = leer_archivo(archivo_entrada)
    if texto is not None:
        numero_digitos = contar_digitos(texto)
        escribir_resultado(archivo_salida, numero_digitos)
        return numero_digitos
    return None

if __name__ == "__main__":
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_digitos.txt'
    numero_digitos = procesar_archivo(archivo_entrada, archivo_salida)
    print(f"El archivo contiene {numero_digitos} dígitos. El resultado se ha guardado en {archivo_salida}.")
