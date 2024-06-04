def escribir_archivo(archivo, contenido):
    try:
        with open(archivo, 'w') as f:
            f.write(contenido)
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo}': {e}")
