# generar_estadisticas.py
def generar_estadisticas(palabras):
    if not palabras:
        return {}

    total_palabras = len(palabras)
    longitudes = [len(palabra) for palabra in palabras]
    longitud_media = sum(longitudes) / total_palabras
    palabra_mas_larga = max(palabras, key=len)
    palabra_mas_corta = min(palabras, key=len)

    return {
        'total_palabras': total_palabras,
        'longitud_media': longitud_media,
        'palabra_mas_larga': palabra_mas_larga,
        'palabra_mas_corta': palabra_mas_corta
    }
