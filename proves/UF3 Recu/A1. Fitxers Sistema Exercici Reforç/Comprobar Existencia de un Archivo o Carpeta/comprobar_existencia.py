import os

def comprobar_existencia(ruta):
    if os.path.exists(ruta):
        if os.path.isfile(ruta):
            return "El archivo existe."
        elif os.path.isdir(ruta):
            return "La carpeta existe."
    else:
        return "El archivo o carpeta no existe."

def obtener_rutas(ruta):
    ruta_absoluta = os.path.abspath(ruta)
    ruta_relativa = os.path.relpath(ruta)
    return ruta_absoluta, ruta_relativa
