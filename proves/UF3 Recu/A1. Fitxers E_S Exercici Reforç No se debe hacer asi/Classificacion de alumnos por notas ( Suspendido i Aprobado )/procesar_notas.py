def procesar_notas(lista_notas):
    aprobados = []
    suspendidos = []
    for linea in lista_notas:
        nombre, nota = linea.strip().split(', ')
        nota = float(nota)
        if 5 <= nota <= 10:
            aprobados.append((nombre, nota))
        elif 0 <= nota < 5:
            suspendidos.append((nombre, nota))
    return aprobados, suspendidos
