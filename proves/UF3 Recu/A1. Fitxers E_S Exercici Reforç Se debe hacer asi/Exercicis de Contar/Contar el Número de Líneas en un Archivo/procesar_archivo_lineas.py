from leer_archivo import leer_archivo
from contar_lineas import contar_lineas
from escribir_resultado import escribir_resultado

def procesar_archivo(archivo_entrada, archivo_salida):
    texto = leer_archivo(archivo_entrada)
    if texto is not None:
        numero_lineas = contar_lineas(texto)
        escribir_resultado(archivo_salida, numero_lineas)
        return numero_lineas
    return None
