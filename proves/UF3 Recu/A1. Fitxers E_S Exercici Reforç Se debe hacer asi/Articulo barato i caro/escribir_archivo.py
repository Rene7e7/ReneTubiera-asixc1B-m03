def escribir_articulos(archivo_salida, lista_articulos):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for articulo, precio in lista_articulos:
                archivo.write(f"{articulo}: {precio}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
