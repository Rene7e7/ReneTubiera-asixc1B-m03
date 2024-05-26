from lectura import leer_archivo
from escritura import escribir_archivo

def unir_lineas(archivo_entrada, archivo_salida):
    lineas = leer_archivo(archivo_entrada)
    if lineas is None:
        return
    contenido_unido = ' '.join(lineas)
    escribir_archivo(archivo_salida, contenido_unido)
