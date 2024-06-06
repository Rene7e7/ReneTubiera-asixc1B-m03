from leer_archivo import leer_archivo
from contar_palabras import contar_palabras
from escribir_resultado import escribir_resultado

def procesar_archivo(archivo_entrada, archivo_salida):
    texto = leer_archivo(archivo_entrada)
    if texto is not None:
        numero_palabras = contar_palabras(texto)
        escribir_resultado(archivo_salida, numero_palabras)
        return numero_palabras
    return None
