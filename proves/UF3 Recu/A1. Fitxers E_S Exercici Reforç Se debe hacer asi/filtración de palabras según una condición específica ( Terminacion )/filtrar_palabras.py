import string

def filtrar_palabras(lineas):
    palabras_terminacion = []
    otras_palabras = []

    # Caracteres especiales que queremos eliminar
    caracteres_especiales = string.punctuation + '¿¡' + '“”'  # Añade aquí cualquier otro carácter especial que desees eliminar

    # Lo que se hace es recorrer las líneas
    for linea in lineas:
        # Se divide la línea en palabras
        palabras = linea.split()
        # Se recorren las palabras
        for palabra in palabras:
            # Eliminar caracteres especiales de la palabra
            palabra_limpia = ''.join(caracter for caracter in palabra if caracter not in caracteres_especiales)
            # Se comprueba si la palabra termina en 'ción'
            if palabra_limpia.endswith('al'):
                # Si termina en 'ción' se añade a la lista de palabras_terminacion
                palabras_terminacion.append(palabra_limpia)
            else:
                # Si no termina en 'ción' se añade a la lista de otras_palabras
                otras_palabras.append(palabra_limpia)
    # Se retornan las listas
    return palabras_terminacion, otras_palabras

'''
# Buscar la palabra exacta
import string

def filtrar_palabras(lineas):
    palabras_terminacion = []
    otras_palabras = []

    # Palabra objetivo
    palabra_objetivo = "desarrollo"  # Modifica esta variable según la palabra que deseas buscar

    # Caracteres especiales que queremos eliminar
    caracteres_especiales = string.punctuation + '¿¡' + '“”'  # Añade aquí cualquier otro carácter especial que desees eliminar

    # Lo que se hace es recorrer las líneas
    for linea in lineas:
        # Se divide la línea en palabras
        palabras = linea.split()
        # Se recorren las palabras
        for palabra in palabras:
            # Eliminar caracteres especiales de la palabra
            palabra_limpia = ''.join(caracter for caracter in palabra if caracter not in caracteres_especiales)
            # Se compara la palabra con la palabra objetivo
            if palabra_limpia == palabra_objetivo:
                # Si coincide con la palabra objetivo se añade a la lista de palabras_terminacion
                palabras_terminacion.append(palabra)
            else:
                # Si no coincide se añade a la lista de otras_palabras
                otras_palabras.append(palabra_limpia)
    # Se retornan las listas
    return palabras_terminacion, otras_palabras

'''
