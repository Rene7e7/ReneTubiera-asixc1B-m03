def buscar_reemplazar(archivo, palabra_buscar, palabra_reemplazar):
    try:
        with open(archivo, "r") as f:
            contenido = f.read()
            nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazar)
        with open(archivo, "w") as f:
            f.write(nuevo_contenido)
        print("Palabra reemplazada correctamente.")
    except FileNotFoundError:
        print("El archivo no existe.")
