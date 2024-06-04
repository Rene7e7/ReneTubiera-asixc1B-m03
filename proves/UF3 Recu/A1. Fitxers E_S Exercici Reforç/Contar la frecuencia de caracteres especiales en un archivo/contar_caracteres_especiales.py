from collections import Counter
import string

def contar_caracteres_especiales(contenido):
    # Definir caracteres especiales como cualquier cosa que no sea letra o número
    caracteres_especiales = set(string.punctuation + string.whitespace)

    # Filtrar los caracteres especiales en el contenido
    solo_caracteres_especiales = [char for char in contenido if char in caracteres_especiales]

    # Contar la frecuencia de cada caracter especial
    contador = Counter(solo_caracteres_especiales)

    return contador
