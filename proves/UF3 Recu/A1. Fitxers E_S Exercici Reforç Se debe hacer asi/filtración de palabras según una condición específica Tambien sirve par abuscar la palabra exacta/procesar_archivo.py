from leer_archivo import leer_archivo
from filtrar_palabras import filtrar_palabras
from escribir_archivo import escribir_archivo

def procesar_archivo(archivo_entrada, archivo_terminaciones, archivo_otras):
    lineas = leer_archivo(archivo_entrada)
    if not lineas:
        print("No se puede procesar el archivo.")
        return

    palabras_terminacion, otras_palabras = filtrar_palabras(lineas)
    escribir_archivo(archivo_terminaciones, palabras_terminacion)
    escribir_archivo(archivo_otras, otras_palabras)
