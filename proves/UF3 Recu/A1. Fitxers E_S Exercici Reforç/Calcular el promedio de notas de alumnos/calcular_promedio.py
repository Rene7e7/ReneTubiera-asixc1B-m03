def calcular_promedio(contenido):
    # Extraer las notas (suponiendo que están separadas por saltos de línea)
    notas = contenido.split()

    try:
        # Convertir las notas a flotantes (si es necesario)
        notas = [float(nota) for nota in notas]
    except ValueError:
        print('El archivo contiene elementos que no son números.')
        return None

    # Calcular el promedio
    promedio = sum(notas) / len(notas) if notas else 0

    return promedio
