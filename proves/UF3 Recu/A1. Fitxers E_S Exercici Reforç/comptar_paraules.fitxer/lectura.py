def llegir_arxiu(ruta):
    try:
        # Lo que fa es obrir el fitxer en mode lectura
        with open(ruta, "r") as f:
            # retorna una llista amb totes les línies del fitxer
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
        return []
