def calcular_longitud_media(palabras):
    if not palabras:
        return 0
    longitudes = [len(palabra) for palabra in palabras]
    longitud_media = sum(longitudes) / len(palabras)
    return longitud_media
