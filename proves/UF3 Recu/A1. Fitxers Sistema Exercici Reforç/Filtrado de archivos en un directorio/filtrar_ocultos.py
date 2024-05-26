import os

def filtrar_ocultos(directorio, ocultos=True):
    archivos_filtrados = []
    for raiz, directorios, archivos in os.walk(directorio):
        if not ocultos:
            archivos = [archivo for archivo in archivos if not archivo.startswith('.')]
        for archivo in archivos:
            archivos_filtrados.append(os.path.join(raiz, archivo))
    return archivos_filtrados
