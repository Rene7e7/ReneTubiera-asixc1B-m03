import re

def procesar_contenido(contenido):
    palabras = []
    numeros = []

    lineas = contenido.splitlines()

    for linea in lineas:
        # Detectar palabras
        palabras_en_linea = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', linea)
        palabras.extend(palabras_en_linea)

        # Detectar números
        numeros_en_linea = re.findall(r'\b\d+\b', linea)
        numeros.extend(numeros_en_linea)

    return "\n".join(palabras), "\n".join(numeros)
