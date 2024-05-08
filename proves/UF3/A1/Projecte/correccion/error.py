import os
import logging

# Configuración del registro
logging.basicConfig(filename="log/boges.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.ERROR)

def error_log():
    directorio_inicial = input("Introduce la ruta del directorio inicial: ")
    fecha = obtener_fecha_actual()
    tiempo_transcurrido = obtener_tiempo_transcurrido()

    logging.info("info message")  # Este mensaje no se registrará en el archivo
    logging.debug("debug message")  # Este mensaje no se registrará en el archivo

    if not os.path.isdir(directorio_inicial):
        print("El directorio especificado no existe.")
        logging.error(f"{fecha} - Error: El directorio especificado no existe. - {tiempo_transcurrido}")
        return

    if not os.access(directorio_inicial, os.R_OK):
        print("No tienes permiso para leer el directorio especificado.")
        logging.error(f"{fecha} - Error: El directorio no tiene permisos para tu usuario. - {tiempo_transcurrido}")
        return

    logging.warning("warn message")  # Este mensaje se registrará como una advertencia
    logging.error("error message")  # Este mensaje se registrará como un error
    logging.critical("critical message")

    print("\nRecorrido del árbol de directorios:")
    recorrer_arbol_directorios(directorio_inicial)
