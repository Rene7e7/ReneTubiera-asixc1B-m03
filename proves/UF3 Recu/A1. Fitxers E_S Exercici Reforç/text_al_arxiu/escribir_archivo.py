def escribir_archivo(ruta, texto):
    try:
        with open(ruta, "w") as archivo:
            archivo.write(texto)
    except Exception as e:
        print(f"Error al escribir en el archivo '{ruta}': {e}")
