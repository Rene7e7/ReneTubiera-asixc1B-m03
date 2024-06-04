def contar_vocales_no_vocales(texto):
    vocales = 'aeiouáéíóúü'
    frecuencia_vocales = {vocal: 0 for vocal in vocales}
    frecuencia_no_vocales = {}

    for caracter in texto.lower():
        if caracter in vocales:
            frecuencia_vocales[caracter] += 1
        elif caracter.isalpha():
            frecuencia_no_vocales[caracter] = frecuencia_no_vocales.get(caracter, 0) + 1

    return frecuencia_vocales, frecuencia_no_vocales
