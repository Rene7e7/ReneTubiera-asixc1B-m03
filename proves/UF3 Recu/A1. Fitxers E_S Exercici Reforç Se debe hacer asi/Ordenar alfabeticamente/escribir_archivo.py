def escribir_lineas(archivo_salida, lineas):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as salida:
            for linea in lineas:
                salida.write(linea)
        print(f"Las líneas se han escrito en '{archivo_salida}' correctamente.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
