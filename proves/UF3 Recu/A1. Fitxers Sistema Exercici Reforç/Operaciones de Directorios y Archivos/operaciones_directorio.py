import os

def crear_directorio(nombre_directorio):
    try:
        os.mkdir(nombre_directorio)
        return f"Directorio '{nombre_directorio}' creado con éxito."
    except FileExistsError:
        return f"Error: el directorio '{nombre_directorio}' ya existe."

def eliminar_directorio(nombre_directorio):
    try:
        os.rmdir(nombre_directorio)
        return f"Directorio '{nombre_directorio}' eliminado con éxito."
    except FileNotFoundError:
        return f"Error: el directorio '{nombre_directorio}' no existe."

def renombrar_directorio(nombre_antiguo, nombre_nuevo):
    try:
        os.rename(nombre_antiguo, nombre_nuevo)
        return f"Directorio '{nombre_antiguo}' renombrado a '{nombre_nuevo}'."
    except FileNotFoundError:
        return f"Error: el directorio '{nombre_antiguo}' no existe."

def cambiar_permisos(nombre_directorio, permisos):
    try:
        os.chmod(nombre_directorio, permisos)
        return f"Permisos del directorio '{nombre_directorio}' cambiados a {oct(permisos)}."
    except FileNotFoundError:
        return f"Error: el directorio '{nombre_directorio}' no existe."

# Funciones similares para archivos (crear_archivo, eliminar_archivo, renombrar_archivo, cambiar_permisos_archivo)
