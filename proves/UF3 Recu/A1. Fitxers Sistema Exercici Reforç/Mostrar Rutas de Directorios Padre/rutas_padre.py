import os

def mostrar_rutas_padre(ruta):
    ruta_actual = os.path.abspath(ruta)
    while ruta_actual != os.path.dirname(ruta_actual):
        print(ruta_actual)
        ruta_actual = os.path.dirname(ruta_actual)
    print(ruta_actual)

