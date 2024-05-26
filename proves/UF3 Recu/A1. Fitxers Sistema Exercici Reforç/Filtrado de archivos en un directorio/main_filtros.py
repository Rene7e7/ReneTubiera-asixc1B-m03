from filtrar_por_extension import filtrar_por_extension
from filtrar_por_nombre import filtrar_por_nombre
from filtrar_ocultos import filtrar_ocultos

def filtrar_archivos(directorio, extension="", nombre="", ocultos=True):
    archivos_filtrados = []
    if extension:
        archivos_filtrados.extend(filtrar_por_extension(directorio, extension))
    if nombre:
        archivos_filtrados.extend(filtrar_por_nombre(directorio, nombre))
    if not ocultos:
        archivos_filtrados.extend(filtrar_ocultos(directorio, ocultos))
    return archivos_filtrados

def main():
    directorio = "."  # Directorio actual
    extension = "txt"  # Extensión a filtrar
    nombre = "test"    # Nombre a filtrar
    ocultos = True     # Incluir archivos ocultos

    archivos_filtrados = filtrar_archivos(directorio, extension, nombre, ocultos)
    print("Archivos filtrados:")
    for archivo in archivos_filtrados:
        print(archivo)

if __name__ == "__main__":
    main()
