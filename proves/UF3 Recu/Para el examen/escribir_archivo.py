def escribir_archivo(archivo_salida, lineas):
    """Escribe una lista de líneas en un archivo."""
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                archivo.write(linea)
        print(f"Contenido guardado en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
