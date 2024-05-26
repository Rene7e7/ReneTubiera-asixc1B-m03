def eliminar_lineas_vacias(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as f:
            lineas = [linea.strip() for linea in f.readlines() if linea.strip()]
        with open(ruta_archivo, "w") as f:
            f.write("\n".join(lineas))
    except FileNotFoundError:
        print("El archivo no se encuentra.")
    except PermissionError:
        print("No tienes permiso para acceder al archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
