def combinar_archivos(archivo1, archivo2, archivo_combinado):
    try:
        with open(archivo1, "r") as f1, open(archivo2, "r") as f2, open(archivo_combinado, "w") as f_combinado:
            f_combinado.write(f1.read())
            f_combinado.write(f2.read())
        print("Archivos combinados correctamente.")
    except FileNotFoundError:
        print("Uno de los archivos no se encuentra.")
    except PermissionError:
        print("No tienes permiso para combinar los archivos.")
    except Exception as e:
        print(f"Error inesperado: {e}")
