def buscar_palabra(archivo, palabra_buscar):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            for i, linea in enumerate(lineas, start=1):
                if palabra_buscar in linea:
                    print(f"Línea {i}: {linea.strip()}")
    except FileNotFoundError:
        print("El archivo no existe.")
