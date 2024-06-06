# crear_indice_invertido.py
from collections import defaultdict

def crear_indice_invertido(palabras):
    indice_invertido = defaultdict(set)
    for palabra in palabras:
        for letra in palabra:
            indice_invertido[letra].add(palabra)
    return {letra: list(palabras) for letra, palabras in indice_invertido.items()}
