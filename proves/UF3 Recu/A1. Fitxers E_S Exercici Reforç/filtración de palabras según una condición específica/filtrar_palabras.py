def filtrar_palabras(lineas):
    palabras_terminacion = []
    otras_palabras = []
    # lo que se hace es recorrer las lineas
    for linea in lineas:
        # se divide la linea en palabras
        palabras = linea.split()
        # se recorren las palabras
        for palabra in palabras:
            # se comprueba si la palabra termina en 'ción'
            if palabra.endswith('ción'):  # Asegúrate de usar 'ción' con tilde
                # si termina en 'ción' se añade a la lista de palabras_terminacion
                palabras_terminacion.append(palabra)
            else:
                # si no termina en 'ción' se añade a la lista de otras_palabras
                otras_palabras.append(palabra)
    # se retornan las listas
    return palabras_terminacion, otras_palabras
