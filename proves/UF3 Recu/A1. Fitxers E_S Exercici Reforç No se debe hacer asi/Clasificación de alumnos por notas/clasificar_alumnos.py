def clasificar_alumnos(contenido):
    lineas = contenido.splitlines()
    clasificaciones = {
        'suspenso': [],
        'bien': [],
        'notable': [],
        'excelente': []
    }

    for linea in lineas:
        nombre, nota_str = linea.split(',')
        nota = float(nota_str.strip())

        if nota < 5:
            clasificaciones['suspenso'].append((nombre, nota))
        elif nota in [5, 6]:
            clasificaciones['bien'].append((nombre, nota))
        elif nota in [7, 8]:
            clasificaciones['notable'].append((nombre, nota))
        elif nota in [9, 10]:
            clasificaciones['excelente'].append((nombre, nota))

    return clasificaciones
