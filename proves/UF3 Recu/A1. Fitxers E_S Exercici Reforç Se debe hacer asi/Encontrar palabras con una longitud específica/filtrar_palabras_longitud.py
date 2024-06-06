# filtrar_palabras_longitud.py
def filtrar_palabras_longitud(palabras, longitud):
    return [palabra for palabra in palabras if len(palabra) == longitud]
