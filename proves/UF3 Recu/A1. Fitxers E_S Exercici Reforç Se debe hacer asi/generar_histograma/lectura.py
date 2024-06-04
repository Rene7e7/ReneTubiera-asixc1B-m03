def leer_notas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
        return None
