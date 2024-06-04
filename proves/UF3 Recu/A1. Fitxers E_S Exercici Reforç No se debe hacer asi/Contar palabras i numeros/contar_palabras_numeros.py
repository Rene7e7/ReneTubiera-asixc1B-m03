import re

def contar_palabras(texto):
    palabras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', texto)
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra.lower() in frecuencia_palabras:
            frecuencia_palabras[palabra.lower()] += 1
        else:
            frecuencia_palabras[palabra.lower()] = 1
    return frecuencia_palabras

def contar_numeros(texto):
    numeros = re.findall(r'\b\d+\b', texto)
    frecuencia_numeros = {}
    for numero in numeros:
        if numero in frecuencia_numeros:
            frecuencia_numeros[numero] += 1
        else:
            frecuencia_numeros[numero] = 1
    return frecuencia_numeros
