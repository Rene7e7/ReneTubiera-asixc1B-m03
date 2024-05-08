def archivo_vacio(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as f:
            return not f.read()
    except FileNotFoundError:
        print("El archivo no se encuentra.")
    except PermissionError:
        print("No tienes permiso para acceder al archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
