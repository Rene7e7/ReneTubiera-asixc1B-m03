def ordenar_palabras(archivo):
    try:
        with open(archivo, "r") as f:
            palabras = f.read().split()
            palabras.sort()
        with open(archivo, "w") as f:
            for palabra in palabras:
                f.write(f"{palabra}\n")
    except FileNotFoundError:
        print("El archivo no existe.")
