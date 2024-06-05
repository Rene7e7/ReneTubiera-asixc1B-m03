from leer_archivo import leer_archivo
from escribir_archivo import escribir_archivo

def procesar_archivo(archivo_entrada, archivo_salida, funcion_procesamiento):
    """Lee un archivo, procesa su contenido, y escribe el resultado en otro archivo.

    :param archivo_entrada: Ruta del archivo de entrada.
    :param archivo_salida: Ruta del archivo de salida.
    :param funcion_procesamiento: Función que procesa el texto del archivo.
    """
    texto = leer_archivo(archivo_entrada)
    if texto is not None:
        resultado = funcion_procesamiento(texto)
        escribir_archivo(archivo_salida, resultado)
        return resultado
    return None
