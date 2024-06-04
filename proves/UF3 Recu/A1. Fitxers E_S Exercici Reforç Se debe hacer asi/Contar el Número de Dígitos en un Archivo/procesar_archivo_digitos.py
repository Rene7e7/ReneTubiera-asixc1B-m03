from leer_archivo import leer_archivo
from contar_digitos import contar_digitos
from escribir_resultado import escribir_resultado

def procesar_archivo(archivo_entrada, archivo_salida):
    texto = leer_archivo(archivo_entrada)
    # Si el texto no es None
    if texto is not None:
        # Contamos los dígitos del texto
        numero_digitos = contar_digitos(texto)
        # Escribimos el resultado en el archivo de salida
        escribir_resultado(archivo_salida, numero_digitos)
        # Retornamos el número de dígitos
        return numero_digitos
    return None
