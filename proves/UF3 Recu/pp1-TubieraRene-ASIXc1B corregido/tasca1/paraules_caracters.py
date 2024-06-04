from lectura import leer_archivo
from escritura import escribir_archivo

def palabras(archivo, longitud):
    # Contar palabras de longitud 'longitud'
    palabras_contador = []
    try:
        # Leer archivo y contar palabras de longitud 'longitud'
        palabras_contador = [palabra.strip() for palabra in leer_archivo(archivo) if len(palabra.strip()) == longitud]
        archivo_salida = f"palabras-{longitud}.txt"
        escribir_archivo(archivo_salida, palabras_contador)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    return palabras_contador
