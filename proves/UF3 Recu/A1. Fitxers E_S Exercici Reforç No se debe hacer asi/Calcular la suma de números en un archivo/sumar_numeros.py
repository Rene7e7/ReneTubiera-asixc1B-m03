def sumar_numeros(contenido):
    numeros = contenido.split()

    try:
        numeros = [float(num) for num in numeros]
    except ValueError:
        print('El archivo contiene elementos que no son números.')
        return None

    suma_total = sum(numeros)
    return suma_total
