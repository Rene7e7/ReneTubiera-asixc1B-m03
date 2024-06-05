import re

def procesar_contenido(contenido):
    resultados = []

    lineas = contenido.splitlines()

    for indice, linea in enumerate(lineas, start=1):
        # Detectar palabras
        palabras = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', linea)
        # Detectar números
        numeros = re.findall(r'\b\d+\b', linea)

        resultados.append(f"Línea {indice}: {len(palabras)} palabras, {len(numeros)} números")

    return "\n".join(resultados)
