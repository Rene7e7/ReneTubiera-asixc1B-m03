def escribir_archivo(archivo_salida, contenido):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
