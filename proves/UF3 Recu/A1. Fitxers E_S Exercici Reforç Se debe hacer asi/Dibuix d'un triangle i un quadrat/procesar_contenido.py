def procesar_contenido(lineas):
    barras_inclinadas = 0
    barras_invertidas = 0
    lineas_buides = 0

    for linea in lineas:
        if '/' in linea:
            barras_inclinadas += 1
        if '\\' in linea:
            barras_invertidas += 1
        if linea.strip() == '':
            lineas_buides += 1

    return barras_inclinadas, barras_invertidas, lineas_buides
