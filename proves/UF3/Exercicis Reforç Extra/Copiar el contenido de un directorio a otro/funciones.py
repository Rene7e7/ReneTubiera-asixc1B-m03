import os
import shutil

def copiar_directorio(origen, destino):
    try:
        if os.path.exists(destino):
            print(f"El directorio de destino {destino} ya existe.")
        else:
            shutil.copytree(origen, destino)
            print("Directorio copiado correctamente.")
    except FileNotFoundError:
        print("El directorio de origen no se encuentra.")
    except PermissionError:
        print("No tienes permiso para copiar el directorio.")
    except Exception as e:
        print(f"Error inesperado: {e}")
