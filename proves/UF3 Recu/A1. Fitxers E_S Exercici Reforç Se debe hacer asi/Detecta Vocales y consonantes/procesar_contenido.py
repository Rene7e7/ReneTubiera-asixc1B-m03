import re

def procesar_contenido(contenido):
    resultados = []

    lineas = contenido.splitlines()

    for indice, linea in enumerate(lineas, start=1):
        # Detectar palabras
        palabras = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', linea)
        # Detectar números
        numeros = re.findall(r'\b\d+\b', linea)
        # Detectar caracteres especiales
        caracteres_especiales = re.findall(r'[^A-Za-zÀ-ÖØ-öø-ÿ\d\s]', linea)
        # Detectar vocales y consonantes
        vocales = re.findall(r'[AEIOUaeiouÀ-ÖØ-öø-ÿ]', linea)
        consonantes = re.findall(r'[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]', linea)

        resultados.append(
            f"Línea {indice}: {len(palabras)} palabras, {len(numeros)} números, {len(caracteres_especiales)} caracteres especiales, "
            f"{len(vocales)} vocales, {len(consonantes)} consonantes"
        )

    return "\n".join(resultados)
