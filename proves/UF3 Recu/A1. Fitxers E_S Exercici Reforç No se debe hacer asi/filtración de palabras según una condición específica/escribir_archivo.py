def escribir_archivo(archivo_salida, palabras):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for palabra in palabras:
                archivo.write(palabra + '\n')
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
