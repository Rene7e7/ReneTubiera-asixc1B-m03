def procesar_contenido(contenido):
    caracteres_especiales = []

    for caracter in contenido:
        if not caracter.isalnum() and not caracter.isspace():
            caracteres_especiales.append(caracter)

    return "".join(caracteres_especiales)
