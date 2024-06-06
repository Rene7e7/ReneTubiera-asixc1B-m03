def filtrar_palabras_palindromas(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]
