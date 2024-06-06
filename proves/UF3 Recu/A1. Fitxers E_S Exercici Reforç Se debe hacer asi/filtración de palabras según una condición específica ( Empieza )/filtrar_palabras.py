# filtrar_palabras.py
import string

def filtrar_palabras(lineas, inicio):
    palabras_inicio = []
    otras_palabras = []

    # Caracteres especiales que queremos eliminar
    caracteres_especiales = string.punctuation + '¿¡' + '“”'

    # Recorrer las líneas
    for linea in lineas:
        # Dividir la línea en palabras
        palabras = linea.split()
        # Recorrer las palabras
        for palabra in palabras:
            # Eliminar caracteres especiales de la palabra
            palabra_limpia = ''.join(caracter for caracter in palabra if caracter not in caracteres_especiales)
            # Comprobar si la palabra comienza con la secuencia especificada
            if palabra_limpia.startswith(inicio):
                # Si comienza con la secuencia, añadir a la lista de palabras_inicio
                palabras_inicio.append(palabra_limpia)
            else:
                # Si no comienza con la secuencia, añadir a la lista de otras_palabras
                otras_palabras.append(palabra_limpia)
    # Retornar las listas
    return palabras_inicio, otras_palabras
