import re
def procesar_contenido(contenido):
    palabras = []
    numeros = []
    caracteres_especiales = []

    lineas = contenido.splitlines()

    for linea in lineas:
        palabras_en_linea = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', linea)  # Detecta solo palabras
        palabras.extend(palabras_en_linea)

        for caracter in linea:
            if caracter.isdigit():
                numeros.append(caracter)
            elif not caracter.isspace() and not caracter.isalnum():
                caracteres_especiales.append(caracter)

    return "\n".join(palabras), "\n".join(numeros), "\n".join(caracteres_especiales)
