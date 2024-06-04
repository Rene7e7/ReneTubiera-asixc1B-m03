from collections import Counter

def contar_vocales_no_vocales(texto):
    vocales = 'aeiouáéíóúü'
    frecuencia_vocales = {vocal: 0 for vocal in vocales}
    frecuencia_no_vocales = {}

    for caracter in texto.lower():
        if caracter in vocales:
            frecuencia_vocales[caracter] += 1
        elif caracter.isalpha():
            frecuencia_no_vocales[caracter] = frecuencia_no_vocales.get(caracter, 0) + 1

    return frecuencia_vocales, frecuencia_no_vocales

def escribir_resultados(archivo_vocales, archivo_no_vocales, frecuencia_vocales, frecuencia_no_vocales):
    try:
        with open(archivo_vocales, 'w', encoding='utf-8') as archivo:
            for vocal, frecuencia in frecuencia_vocales.items():
                archivo.write(f'{vocal}: {frecuencia}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_vocales}': {e}")

    try:
        with open(archivo_no_vocales, 'w', encoding='utf-8') as archivo:
            for no_vocal, frecuencia in frecuencia_no_vocales.items():
                archivo.write(f'{no_vocal}: {frecuencia} veces\n')
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
        return None

# Asegúrate de que las funciones estén definidas aquí o importadas correctamente
if __name__ == "__main__":
    texto = leer_archivo('texto.txt')
    if texto:
        frecuencia_vocales, frecuencia_no_vocales = contar_vocales_no_vocales(texto)
        escribir_resultados('vocales.txt', 'no_vocales.txt', frecuencia_vocales, frecuencia_no_vocales)
