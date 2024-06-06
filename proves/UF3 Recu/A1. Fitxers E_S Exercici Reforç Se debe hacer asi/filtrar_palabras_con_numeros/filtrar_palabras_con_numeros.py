def filtrar_palabras_con_numeros(palabras):
    return [palabra for palabra in palabras if any(char.isdigit() for char in palabra)]
