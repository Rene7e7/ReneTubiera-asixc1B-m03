import random

# Lista de caracteres especiales
LISTA = [".", ",", ";", ":", "?", "!", "¿", "¡", "(", ")", "[", "]", "{", "}", "'", '"', "-", "_", "*", "/", "&", "%", "=", "+", "|", "<", ">", "@", "#", "$"]

def dividir(oracion):
    """Divide la oración en palabras."""
    return oracion.split()

def identificar_paraules(paraules):
    """Identifica las palabras con más de 3 letras para ser desordenadas."""
    palabras_desordenadas = []
    for paraula in paraules:
        if len(paraula) > 3:
            palabras_desordenadas.append(paraula)
    return palabras_desordenadas

def identificar_caracters_especials(paraula):
    """Identifica los caracteres especiales en una palabra."""
    caracters_especials = []
    for i, lletra in enumerate(paraula):
        if lletra in LISTA:
            caracters_especials.append((lletra, i))
    return caracters_especials

def aleatorizar_parte_medio(paraula):
    """Aleatoriza el orden de los caracteres en el medio de la palabra."""
    caracters_especials = identificar_caracters_especials(paraula)
    part_inicial = paraula[0]
    part_final = paraula[-1]

    # Si es un número, correo electrónico o enlace web, no se altera
    if paraula.isdigit() or '@' in paraula or paraula.startswith('http://') or paraula.startswith('https://'):
        return paraula

    medio = list(paraula[1:-1])
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

def juntar_palabras(palabras):
    """Junta las palabras de la lista en una frase."""
    frase = ""
    for elem in palabras:
        frase += elem + " "
    return frase.strip()
