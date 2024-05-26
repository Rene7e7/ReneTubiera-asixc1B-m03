def contar_palabras(archivo):
    try:
        with open(archivo, "r") as f:
            contenido = f.read()
            palabras = len(contenido.split())
            return palabras
    except FileNotFoundError:
        print("El archivo no existe.")
        return 0
