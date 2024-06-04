def encontrar_palabra_mas_frecuente(contenido):
    palabras = contenido.split()
    contador = Counter(palabras)
    palabra_mas_frecuente, frecuencia = contador.most_common(1)[0]
    return palabra_mas_frecuente, frecuencia

def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(f'{resultado}\n')
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

# Asegúrate de que las funciones estén definidas aquí o importadas correctamente
if __name__ == "__main__":
    texto = leer_archivo('texto.txt')
    if texto:
        palabra_mas_frecuente, frecuencia = encontrar_palabra_mas_frecuente(texto)
        escribir_resultado('resultado_palabra_mas_frecuente.txt', f'La palabra más frecuente es: "{palabra_mas_frecuente}" con {frecuencia} apariciones')
