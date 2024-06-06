# main.py
from leer_archivo import leer_archivo
from agrupar_y_ordenar_palabras import agrupar_y_ordenar_palabras
from escribir_grupos import escribir_grupos

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'palabras_por_longitud.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    grupos = agrupar_y_ordenar_palabras(palabras)
    escribir_grupos(archivo_salida, grupos)

    print("Proceso completado. Las palabras agrupadas por longitud y ordenadas por frecuencia se han guardado correctamente.")

if __name__ == "__main__":
    main()
