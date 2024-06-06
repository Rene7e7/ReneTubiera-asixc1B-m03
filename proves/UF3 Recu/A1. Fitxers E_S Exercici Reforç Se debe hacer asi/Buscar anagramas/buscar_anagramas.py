# buscar_anagramas.py
from collections import defaultdict

def buscar_anagramas(palabras):
    anagramas = defaultdict(list)
    for palabra in palabras:
        clave = ''.join(sorted(palabra))
        anagramas[clave].append(palabra)

    # Filtrar para mantener solo los grupos con más de un anagrama
    return {clave: anagramas[clave] for clave in anagramas if len(anagramas[clave]) > 1}
