def buscar_palabra(ruta_archivo, palabra):
    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            if palabra in contenido:
                print(f"La palabra '{palabra}' se encuentra en el archivo.")
            else:
                print(f"La palabra '{palabra}' no se encuentra en el archivo.")
    except FileNotFoundError:
        print("El archivo no se encuentra.")
    except PermissionError:
        print("No tienes permiso para leer el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
