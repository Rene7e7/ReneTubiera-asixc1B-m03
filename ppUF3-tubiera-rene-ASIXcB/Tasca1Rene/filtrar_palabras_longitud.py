def filtrar_palabras_longitud(palabras, longitud):
    # Itera paraula per paraules on conta cararcater per caracter la paraule i si la longitud es 15 la paraula ho retorna
    return [palabra for palabra in palabras if len(palabra) == longitud]