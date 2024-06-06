# agrupar_y_ordenar_palabras.py
from collections import defaultdict, Counter

def agrupar_y_ordenar_palabras(palabras):
    grupos = defaultdict(list)
    for palabra in palabras:
        grupos[len(palabra)].append(palabra)

    for longitud in grupos:
        contador = Counter(grupos[longitud])
        grupos[longitud] = sorted(contador.items(), key=lambda x: (-x[1], x[0]))  # Ordenar por frecuencia y luego alfabéticamente

    return grupos
