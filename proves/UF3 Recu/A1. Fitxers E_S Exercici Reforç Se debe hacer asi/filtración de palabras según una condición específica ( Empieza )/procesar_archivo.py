# procesar_archivo.py
from leer_archivo import leer_archivo
from filtrar_palabras import filtrar_palabras
from escribir_archivo import escribir_archivo

def procesar_archivo(archivo_entrada, archivo_inicio, archivo_otras, inicio):
    lineas = leer_archivo(archivo_entrada)
    if not lineas:
        print("No se puede procesar el archivo.")
        return

    palabras_inicio, otras_palabras = filtrar_palabras(lineas, inicio)
    escribir_archivo(archivo_inicio, palabras_inicio)
    escribir_archivo(archivo_otras, otras_palabras)
