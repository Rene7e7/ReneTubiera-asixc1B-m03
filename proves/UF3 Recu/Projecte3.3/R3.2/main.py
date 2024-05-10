import funcion
import log
import os

def procesar_archivo(archivo_entrada):
    """Procesa un archivo de entrada y genera un archivo de salida con el mismo nombre pero añadiendo _boges."""
    archivo_salida = os.path.join("sortida", os.path.basename(archivo_entrada).replace(".txt", "_boges.txt"))

    # Verificar si el archivo de entrada existe
    if not os.path.isfile(archivo_entrada):
        log.registrar_error("El archivo {} no existe".format(archivo_entrada))
        return

    try:
        # Leer el contenido del archivo de entrada
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
    except Exception as e:
        log.registrar_error("Error al leer el archivo {}: {}".format(archivo_entrada, str(e)))
        return

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

    try:
        # Escribir las líneas aleatorizadas en el archivo de salida
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.writelines(lineas_aleatorizadas)
        log.log("El archivo {} ha sido procesado correctamente".format(archivo_entrada))
    except Exception as e:
        log.registrar_error("Error al escribir en el archivo {}: {}".format(archivo_salida, str(e)))

def main():
    # Directorio de entrada y salida
    directorio_entrada = "entrada"
    directorio_salida = "sortida"
    directorio_log = "log"

    # Verificar si existe el directorio de entrada
    if not os.path.isdir(directorio_entrada):
        log.registrar_error("El directorio de entrada {} no existe".format(directorio_entrada))
        return

    # Verificar si existe el directorio de salida, si no existe se crea
    if not os.path.isdir(directorio_salida):
        try:
            os.makedirs(directorio_salida)
        except Exception as e:
            log.registrar_error("Error al crear el directorio de salida {}: {}".format(directorio_salida, str(e)))
            return

    # Verificar si existe el directorio de log, si no existe se crea
    if not os.path.isdir(directorio_log):
        try:
            os.makedirs(directorio_log)
        except Exception as e:
            print("Error al crear el directorio de log {}: {}".format(directorio_log, str(e)))
            return

    log.iniciar_programa()

    # Procesar todos los archivos .txt del directorio de entrada
    for archivo in os.listdir(directorio_entrada):
        if archivo.endswith(".txt"):
            archivo_entrada = os.path.join(directorio_entrada, archivo)
            procesar_archivo(archivo_entrada)

    log.finalizar_programa()

if __name__ == "__main__":
    main()
