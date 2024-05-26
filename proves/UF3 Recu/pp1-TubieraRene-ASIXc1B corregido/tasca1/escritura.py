def escribir_archivo(archivo, contenido):
    try:
        with open(archivo, 'w') as f:
            for palabra in contenido:
                f.write(palabra + '\n')  # Escribir cada palabra en una línea separada
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
