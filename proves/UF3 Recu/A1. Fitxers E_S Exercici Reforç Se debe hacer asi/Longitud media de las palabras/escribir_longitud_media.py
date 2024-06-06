def escribir_longitud_media(archivo_salida, longitud_media):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(f"Longitud media de las palabras: {longitud_media:.2f}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
