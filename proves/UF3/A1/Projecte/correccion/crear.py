import os
def crear_directory():
    directorios = ["sortida", "log"]
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)


crear_directory()
