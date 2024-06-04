from leer_archivo import leer_archivo
from contar_letras import contar_letras
from escribir_resultado import escribir_resultado

def procesar_archivo(archivo_entrada, archivo_salida):
    texto = leer_archivo(archivo_entrada)
    if texto is not None:
        numero_letras = contar_letras(texto)
        escribir_resultado(archivo_salida, numero_letras)
        return numero_letras
    return None
