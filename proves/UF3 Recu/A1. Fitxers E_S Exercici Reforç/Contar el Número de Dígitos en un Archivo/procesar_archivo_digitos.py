from leer_archivo import leer_archivo
from contar_digitos import contar_digitos
from escribir_resultado import escribir_resultado

def procesar_archivo(archivo_entrada, archivo_salida):
    texto = leer_archivo(archivo_entrada)
    if texto is not None:
        numero_digitos = contar_digitos(texto)
        escribir_resultado(archivo_salida, numero_digitos)
        return numero_digitos
    return None
