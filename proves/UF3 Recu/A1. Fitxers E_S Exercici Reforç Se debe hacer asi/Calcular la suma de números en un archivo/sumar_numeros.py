def sumar_numeros(contenido):
    numeros = contenido.split()

    try:
        # Convertir los elementos de la lista a números
        numeros = [float(num) for num in numeros]
    except ValueError:
        print('El archivo contiene elementos que no son números.')
        return None
    # Calcular la suma de los números
    suma_total = sum(numeros)
    # Devolver la suma total
    return suma_total
