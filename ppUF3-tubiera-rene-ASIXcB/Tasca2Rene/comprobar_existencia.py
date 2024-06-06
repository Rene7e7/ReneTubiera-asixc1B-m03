import os

def comprobar_existencia(directorio):
    # Comproba si el directori existeix
    if os.path.exists(directorio):
        # Si existeix l'arxiu podra executar el programa
        if os.path.isfile(directorio):
            return "El archivo si existe."
        # Si existeix la carpeta podra executar el programa
        elif os.path.isdir(directorio):
            return "La carpeta si existe."
    # Sino ens mostrara un missatge de que la carpeta o l'arxiu no existeix
    else:
        return "El archivo o carpeta no existe."

def obtener_rutas(directorio):
    # mostra la ruta absoluta
    ruta_absoluta = os.path.abspath(directorio)
    # mostra la ruta relativa
    ruta_relativa = os.path.relpath(directorio)
    return ruta_absoluta, ruta_relativa
