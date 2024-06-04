from collections import Counter

def contar_vocales(contenido):
    # Definir las vocales
    vocales = "aeiouAEIOU"

    # Filtrar las vocales en el contenido
    solo_vocales = [letra for letra in contenido if letra in vocales]

    # Contar la frecuencia de cada vocal
    contador = Counter(solo_vocales)

    return contador
