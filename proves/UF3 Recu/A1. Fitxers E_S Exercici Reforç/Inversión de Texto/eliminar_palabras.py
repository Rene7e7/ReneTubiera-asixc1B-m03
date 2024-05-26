from lectura import leer_archivo
from escritura import escribir_archivo

def eliminar_palabras(archivo_entrada, archivo_salida, palabra):
    contenido = leer_archivo(archivo_entrada)
    if contenido is not None:
        contenido_modificado = contenido.replace(palabra, '')
        escribir_archivo(archivo_salida, contenido_modificado)
