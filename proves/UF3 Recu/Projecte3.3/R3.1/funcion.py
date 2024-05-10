import random

# Lista de caracteres especiales
LISTA = [".", ",", ";", ":", "?", "!", "¿", "¡", "(", ")", "[", "]", "{", "}", "'", '"', "-", "_", "*", "/", "&", "%", "=", "+", "|", "<", ">", "@", "#", "$"]

def identificar_paraules(linea):
    """Identifica las palabras con más de 3 letras para ser desordenadas."""
    palabras_desordenadas = []
    palabras = linea.split()
    for palabra in palabras:
        if len(palabra) > 3:
            palabras_desordenadas.append(palabra)
    return palabras_desordenadas

def identificar_caracters_especials(palabra):
    """Identifica los caracteres especiales en una palabra."""
    caracters_especials = []
    for i, lletra in enumerate(palabra):
        if lletra in LISTA:
            caracters_especials.append((lletra, i))
    return caracters_especials

def aleatorizar_parte_medio(palabra):
    """Aleatoriza el orden de los caracteres en el medio de la palabra."""
    caracters_especials = identificar_caracters_especials(palabra)
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
    for char, pos in caracters_especials:
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

def juntar_palabras(lista):
    """Junta las palabras de la lista en una frase."""
    return " ".join(lista)
