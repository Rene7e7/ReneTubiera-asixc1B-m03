# leer_archivo.py
def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo {ruta} no se encuentra.")
        return None
