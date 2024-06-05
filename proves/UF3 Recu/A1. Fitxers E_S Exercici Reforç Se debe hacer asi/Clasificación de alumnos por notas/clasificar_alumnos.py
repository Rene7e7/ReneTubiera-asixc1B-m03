def clasificar_alumnos(contenido):
    # Dividir el contenido del archivo en líneas
    lineas = contenido.splitlines()
    # Crear un diccionario para almacenar las clasificaciones
    clasificaciones = {
        'suspenso': [],
        'bien': [],
        'notable': [],
        'excelente': []
    }
    # Iterar sobre las líneas del archivo
    for linea in lineas:
        # Dividir la línea en el nombre y la nota
        nombre, nota_str = linea.split(',')
        # Convertir la nota a un número decimal
        nota = float(nota_str.strip())

        # Clasificar a los alumnos según su nota
        if nota < 5:
            # Añadir el nombre y la nota a la lista de suspensos
            clasificaciones['suspenso'].append((nombre, nota))
        elif nota in [5, 6]:
            # Añadir el nombre y la nota a la lista de bien
            clasificaciones['bien'].append((nombre, nota))
        elif nota in [7, 8]:
            # Añadir el nombre y la nota a la lista de notable
            clasificaciones['notable'].append((nombre, nota))
        elif nota in [9, 10]:
            # Añadir el nombre y la nota a la lista de excelente
            clasificaciones['excelente'].append((nombre, nota))
    # Devolver el diccionario con las clasificaciones
    return clasificaciones
