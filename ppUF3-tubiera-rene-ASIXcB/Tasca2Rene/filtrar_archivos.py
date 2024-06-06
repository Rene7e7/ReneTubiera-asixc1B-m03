from filtrar_por_extension import filtrar_por_extension
def filtrar_archivos(directorio, extension=""):
    # On es guarda els fitxers filtrats amb l'extensio especificat ("py")
    archivos_filtrados = []
    # Si la extensio acaba en py
    if extension:
        # Extendra els arxius filtrats amb l'extensio, mostrant la ruta absoluta o relativa i al costat es mostra nom del fitxer amb l'extensio especificat ¡
        archivos_filtrados.extend(filtrar_por_extension(directorio, extension))
    # Retorna els arxius filtrats
    return archivos_filtrados