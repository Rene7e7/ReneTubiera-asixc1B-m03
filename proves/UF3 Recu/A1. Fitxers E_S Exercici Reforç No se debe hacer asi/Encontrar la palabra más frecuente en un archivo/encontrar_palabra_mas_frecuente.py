from collections import Counter

def encontrar_palabra_mas_frecuente(contenido):
    palabras = contenido.split()
    contador = Counter(palabras)
    palabra_mas_frecuente, frecuencia = contador.most_common(1)[0]
    return palabra_mas_frecuente, frecuencia
