def procesar_notas(lista_notas):
    aprobados = []
    suspendidos = []
    # Recorrer la lista de notas
    for linea in lista_notas:
        # Separar el nombre y la nota de la línea i separarlos por la coma
        nombre, nota = linea.strip().split(', ')
        # Convertir la nota a un número decimal
        nota = float(nota)
        # Clasificar a los alumnos según su nota
        if 5 <= nota <= 10:
            aprobados.append((nombre, nota))
        elif 0 <= nota < 5:
            suspendidos.append((nombre, nota))
    # Devolver las listas de aprobados y suspendidos
    return aprobados, suspendidos
