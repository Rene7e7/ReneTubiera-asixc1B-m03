import random
from data_sources import LISTA

def aleatorizar_palabra(palabra):
    caracteres_especiales = identificar_caracteres_especiales(palabra)
    part_inicial = palabra[0]
    part_final = palabra[-1]

    # Si es un número, correo electrónico o enlace web, no se altera
    if palabra.isdigit() or '@' in palabra or palabra.startswith('http://') or palabra.startswith('https://'):
        return palabra

    medio = list(palabra[1:-1])
    part_media = []
    for char in medio:
        if char not in LISTA:
            part_media.append(char)
    random.shuffle(part_media)

    # Reensamblar la palabra
    palabra_aleatorizada = part_inicial + "".join(part_media) + part_final

    # Agregar los caracteres especiales
    for char, pos in caracteres_especiales:
        if pos == 0:
            if char not in palabra_aleatorizada:
                palabra_aleatorizada = char + palabra_aleatorizada
        elif pos == len(palabra_aleatorizada):
            if char not in palabra_aleatorizada:
                palabra_aleatorizada = palabra_aleatorizada + char
        else:
            if char not in palabra_aleatorizada:
                palabra_aleatorizada = palabra_aleatorizada[:pos] + char + palabra_aleatorizada[pos:]

    return palabra_aleatorizada

def identificar_caracteres_especiales(palabra):
    caracteres_especiales = []
    for i, letra in enumerate(palabra):
        if letra in LISTA:
            caracteres_especiales.append((letra, i))
    return caracteres_especiales

def aleatorizar_palabras(oracion):
    palabras = oracion.split()
    palabras_desordenadas = []
    for palabra in palabras:
        if len(palabra) > 3:
            palabras_desordenadas.append(aleatorizar_palabra(palabra))
        else:
            palabras_desordenadas.append(palabra)
    return palabras_desordenadas
