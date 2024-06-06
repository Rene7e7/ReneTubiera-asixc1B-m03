import os

def filtrar_por_extension(directorio, extension):
    # Guarda els arxius filtrats
    archivos_filtrados = []
    # itera la raiz, directori, archiu de la ruta del directori
    for raiz, directorios, archivos in os.walk(directorio):
        # Itera arxiu a arxiu
        for archivo in archivos:
            # si el arxiu acaba en l'extensio especificat
            if archivo.endswith(extension):
                # Es guardara en archivos_filtrados
                archivos_filtrados.append(os.path.join(raiz, archivo))
    # Retorna archivos_filtrados
    return archivos_filtrados