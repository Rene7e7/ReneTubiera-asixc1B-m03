def clasificar_alumnos(datos_alumnos):
    mayores_de_edad = []
    menores_de_edad = []

    for dato in datos_alumnos:
        nombre, edad = dato.split(';')
        edad = int(edad)
        if edad >= 18:
            mayores_de_edad.append((nombre, edad))
        else:
            menores_de_edad.append((nombre, edad))

    return mayores_de_edad, menores_de_edad
