def llegir_arxiu(ruta):
    try:
        with open(ruta, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
        return []
