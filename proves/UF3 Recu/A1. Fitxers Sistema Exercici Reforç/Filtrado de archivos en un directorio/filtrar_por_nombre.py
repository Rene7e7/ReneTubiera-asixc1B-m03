import os

def filtrar_por_nombre(directorio, nombre):
    archivos_filtrados = []
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if nombre in archivo:
                archivos_filtrados.append(os.path.join(raiz, archivo))
    return archivos_filtrados
