def guardar_archivo(archivo_salida, texto_modificado):
    try:
        with open(archivo_salida, 'w') as archivo:
            archivo.write(texto_modificado)
    except Exception as e:
        print(f"Error al guardar el archivo '{archivo_salida}': {e}")
