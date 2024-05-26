def filtrar_palabras(lineas):
    palabras_terminacion = []
    otras_palabras = []

    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if palabra.endswith('ción'):  # Asegúrate de usar 'ción' con tilde
                palabras_terminacion.append(palabra)
            else:
                otras_palabras.append(palabra)

    return palabras_terminacion, otras_palabras
