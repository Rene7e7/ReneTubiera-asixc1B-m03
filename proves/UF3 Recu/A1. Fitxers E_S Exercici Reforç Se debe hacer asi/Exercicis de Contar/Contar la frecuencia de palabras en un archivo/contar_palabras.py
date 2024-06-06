from collections import Counter

def contar_palabras(contenido):
    # Extraer las palabras (suponiendo que están separadas por espacios o saltos de línea)
    palabras = contenido.split()

    # Contar la frecuencia de cada palabra
    contador = Counter(palabras)

    return contador
