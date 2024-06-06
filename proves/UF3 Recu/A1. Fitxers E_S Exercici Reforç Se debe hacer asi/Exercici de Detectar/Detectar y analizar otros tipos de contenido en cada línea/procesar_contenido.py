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
        # Detectar direcciones de correo electrónico
        correos_electronicos = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', linea)
        # Detectar URLs
        urls = re.findall(r'https?://[^\s]+', linea)
        # Detectar fechas (simplificado para el formato DD/MM/YYYY)
        fechas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', linea)

        resultados.append(
            f"Línea {indice}: {len(palabras)} palabras, {len(numeros)} números, {len(caracteres_especiales)} caracteres especiales, "
            f"{len(correos_electronicos)} correos electrónicos, {len(urls)} URLs, {len(fechas)} fechas"
        )

    return "\n".join(resultados)
