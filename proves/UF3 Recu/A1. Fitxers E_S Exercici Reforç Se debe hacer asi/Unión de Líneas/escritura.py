def escribir_archivo(archivo, lineas):
    try:
        with open(archivo, 'w') as f:
            for linea in lineas:
                f.write(linea)
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo}': {e}")

