import funcion
import log
import os

def leer_archivo(archivo_entrada):
    """Lee el contenido de un archivo y devuelve una lista de líneas."""
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        log.registrar_error("El archivo {} no existe".format(archivo_entrada))
        return []

def escribir_archivo(archivo_salida, contenido):
    """Escribe el contenido en un archivo."""
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.writelines(contenido)

def main():
    archivo_entrada = "paraules.txt"
    archivo_salida = "paraules_boges.txt"
    archivo_log = "boges.log"

    # Verificar si el archivo de entrada existe
    if not os.path.isfile(archivo_entrada):
        log.registrar_error("El archivo {} no existe".format(archivo_entrada))
        return

    # Leer el contenido del archivo de entrada
    lineas = leer_archivo(archivo_entrada)

    # Verificar si el archivo de entrada está vacío
    if not lineas:
        log.registrar_error("El archivo de entrada {} está vacío".format(archivo_entrada))
        return

    lineas_aleatorizadas = []
    for linea in lineas:
        palabras_desordenadas = funcion.identificar_paraules(linea)
        palabras_aleatorizadas = []
        for palabra in linea.split():
            if palabra in palabras_desordenadas:
                palabras_aleatorizadas.append(funcion.aleatorizar_parte_medio(palabra))
            else:
                palabras_aleatorizadas.append(palabra)
        linea_aleatorizada = funcion.juntar_palabras(palabras_aleatorizadas)
        lineas_aleatorizadas.append(linea_aleatorizada + "\n")

    # Escribir las líneas aleatorizadas en el archivo de salida
    escribir_archivo(archivo_salida, lineas_aleatorizadas)
    log.log("El programa ha finalizado correctamente")

if __name__ == "__main__":
    main()
