def clasificar_articulos(datos_articulos):
    caros = []
    baratos = []

    for articulo, precio_str in datos_articulos:
        precio = float(precio_str)
        if precio >= 100:
            caros.append((articulo, precio))
        else:
            baratos.append((articulo, precio))

    return caros, baratos
