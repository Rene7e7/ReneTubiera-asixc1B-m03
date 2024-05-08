def filtrar_palabras(archivo, longitud):
    try:
        with open(archivo, "r") as f:
            palabras_filtradas = [palabra.strip() for palabra in f if len(palabra.strip()) == longitud]
        with open("palabras_filtradas.txt", "w") as f:
            for palabra in palabras_filtradas:
                f.write(f"{palabra}\n")
    except FileNotFoundError:
        print("El archivo no existe.")
