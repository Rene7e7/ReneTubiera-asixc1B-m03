# reemplazar_letra.py
def reemplazar_letra(palabras, letra_original, letra_nueva):
    return [palabra.replace(letra_original, letra_nueva) for palabra in palabras]
