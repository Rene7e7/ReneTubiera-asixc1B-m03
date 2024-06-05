def escribir_articulos(archivo_salida, lista_articulos):
    try:
        # Escribir la lista de artículos en el archivo de salida
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            # Recorrer la lista de artículos y escribir cada uno en el archivo
            for articulo, precio in lista_articulos:
                # Escribir el artículo y su precio en una línea
                archivo.write(f"{articulo}: {precio}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
