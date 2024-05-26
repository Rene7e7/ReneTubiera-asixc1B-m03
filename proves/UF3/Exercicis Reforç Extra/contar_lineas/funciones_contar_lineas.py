def contar_lineas(archivo):
    try:
        with open(archivo, "r") as f:
            lineas = sum(1 for _ in f)
            return lineas
    except FileNotFoundError:
        print("El archivo no existe.")
        return 0
