import os

def filtrar_por_extension(directorio, extension):
    archivos_filtrados = []
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension):
                archivos_filtrados.append(os.path.join(raiz, archivo))
    return archivos_filtrados
