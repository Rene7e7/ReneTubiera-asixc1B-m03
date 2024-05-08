import os

def eliminar_archivo(ruta_archivo):
    try:
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
            print(f"Archivo {ruta_archivo} eliminado correctamente.")
        else:
            print(f"El archivo {ruta_archivo} no existe.")
    except PermissionError:
        print("No tienes permiso para eliminar el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
