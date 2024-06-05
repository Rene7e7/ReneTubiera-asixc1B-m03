# Importaciones necesarias
from leer_archivo import leer_archivo
from filtrar_palabras import filtrar_palabras
from escribir_archivo import escribir_archivo

# Definición de funciones
def leer_archivo(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return []

def filtrar_palabras(lineas):
    palabras_terminacion = []
    otras_palabras = []
    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if palabra.endswith('ción'):
                palabras_terminacion.append(palabra)
            else:
                otras_palabras.append(palabra)
    return palabras_terminacion, otras_palabras

def escribir_archivo(archivo_salida, palabras):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for palabra in palabras:
                archivo.write(palabra + '\n')
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")

# Función principal que procesa el archivo
def procesar_archivo(archivo_entrada, archivo_terminaciones, archivo_otras):
    lineas = leer_archivo(archivo_entrada)
    if not lineas:
        print("No se puede procesar el archivo.")
        return

    palabras_terminacion, otras_palabras = filtrar_palabras(lineas)
    escribir_archivo(archivo_terminaciones, palabras_terminacion)
    escribir_archivo(archivo_otras, otras_palabras)

# Punto de entrada del programa
if __name__ == "__main__":
    archivo_entrada = 'texto.txt'
    archivo_terminaciones = 'terminaciones.txt'
    archivo_otras = 'otras.txt'

    procesar_archivo(archivo_entrada, archivo_terminaciones, archivo_otras)
    print("Proceso completado. Las palabras se han filtrado y guardado correctamente.")
