def escribir_clasificacion(archivo_salida, alumnos):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for nombre, edad in alumnos:
                archivo.write(f"{nombre}: {edad}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
