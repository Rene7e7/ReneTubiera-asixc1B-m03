def crear_directorio_archivo(nombre_directorio, nombre_archivo, contenido_archivo):
    try:
        os.makedirs(nombre_directorio, exist_ok=True)
        with open(f"{nombre_directorio}/{nombre_archivo}", "w") as f:
            f.write(contenido_archivo)
    except OSError:
        print("Error al crear el directorio o archivo.")
