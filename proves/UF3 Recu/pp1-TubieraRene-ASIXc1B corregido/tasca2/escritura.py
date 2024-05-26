def escribir_archivo(archivo_salida, contenido):
    try:
        with open(archivo_salida, 'w') as archivo:
            for linea in contenido:
                archivo.write(linea)
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
