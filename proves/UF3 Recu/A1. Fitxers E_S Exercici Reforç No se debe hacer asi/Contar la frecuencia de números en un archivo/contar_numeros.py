from collections import Counter

def contar_numeros(contenido):
    # Extraer los números (suponiendo que están separados por espacios o saltos de línea)
    numeros = contenido.split()

    try:
        # Convertir los números a enteros (si es necesario)
        numeros = [int(num) for num in numeros]
    except ValueError:
        print('El archivo contiene elementos que no son números enteros.')
        return None

    # Contar la frecuencia de cada número
    contador = Counter(numeros)

    return contador
