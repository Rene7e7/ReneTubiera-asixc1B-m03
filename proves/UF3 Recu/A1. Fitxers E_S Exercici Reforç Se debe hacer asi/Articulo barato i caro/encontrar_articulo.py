def clasificar_articulos(datos_articulos):
    caros = []
    baratos = []
    # Recorremos la lista de tuplas
    for articulo, precio_str in datos_articulos:
        # Convertimos el precio a float
        precio = float(precio_str)
        # Clasificamos el artículo según el precio si es mayor o igual a 100
        if precio >= 100:
            # Añadimos el artículo a la lista de caros
            caros.append((articulo, precio))
        # Si no es mayor o igual a 100
        else:
            # Añadimos el artículo a la lista de baratos
            baratos.append((articulo, precio))

    return caros, baratos
