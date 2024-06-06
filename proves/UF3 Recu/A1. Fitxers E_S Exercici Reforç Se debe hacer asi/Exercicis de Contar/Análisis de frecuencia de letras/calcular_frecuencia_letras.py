# calcular_frecuencia_letras.py
from collections import Counter

def calcular_frecuencia_letras(palabras):
    contador = Counter()
    for palabra in palabras:
        contador.update(palabra)
    return dict(contador)
