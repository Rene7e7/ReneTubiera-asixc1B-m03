def contar_lineas(texto):
    # Contamos la cantidad de saltos de línea en el texto
    return texto.count('\n')

def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(f"El archivo contiene {resultado} líneas.\n")
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
        numero_lineas = contar_lineas(texto)
        escribir_resultado(archivo_salida, numero_lineas)
        return numero_lineas
    return None

if __name__ == "__main__":
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_lineas.txt'
    numero_lineas = procesar_archivo(archivo_entrada, archivo_salida)
    print(f"El archivo contiene {numero_lineas} líneas. El resultado se ha guardado en {archivo_salida}.")
