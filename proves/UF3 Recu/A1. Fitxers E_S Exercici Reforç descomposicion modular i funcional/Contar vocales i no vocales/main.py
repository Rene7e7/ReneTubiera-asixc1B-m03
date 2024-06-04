def contar_vocales_no_vocales(texto):
    vocales = 'aeiouáéíóúü'
    contador_vocales = 0
    contador_no_vocales = 0

    for caracter in texto.lower():
        if caracter in vocales:
            contador_vocales += 1
        elif caracter.isalpha():
            contador_no_vocales += 1

    return contador_vocales, contador_no_vocales

def escribir_resultados(archivo_vocales, archivo_no_vocales, contador_vocales, contador_no_vocales):
    try:
        with open(archivo_vocales, 'w', encoding='utf-8') as archivo:
            archivo.write(f'Vocales: {contador_vocales}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_vocales}': {e}")

    try:
        with open(archivo_no_vocales, 'w', encoding='utf-8') as archivo:
            archivo.write(f'No vocales: {contador_no_vocales}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_no_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_no_vocales}': {e}")

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
        contador_vocales, contador_no_vocales = contar_vocales_no_vocales(texto)
        escribir_resultados('vocales.txt', 'no_vocales.txt', contador_vocales, contador_no_vocales)
