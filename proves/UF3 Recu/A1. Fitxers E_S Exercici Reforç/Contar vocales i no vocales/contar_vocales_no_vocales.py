def contar_vocales_no_vocales(texto):
    vocales = 'aeiouáéíóúü'
    contador_vocales = 0
    contador_no_vocales = 0

    for caracter in texto.lower():
        if caracter in vocales:
            contador_vocales += 1
        elif caracter.isalpha():
            contador_no_vocales += 1

    return contador_vocales, contador_no_vocales
