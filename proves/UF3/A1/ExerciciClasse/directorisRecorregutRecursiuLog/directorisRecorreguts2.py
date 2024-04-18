'''
Modificar l'exemple Recorregut de directoris recursiu, per a controlat els possibles errors.

Anotar en un fitxer recorregut.log:

 els errors trobats,

qualsevol incidència

el temps transcorregut (per cada execució de programa)

con datatiempo del sistema.

por ejemplo:
import logging



logFile = 'myapp.log'

logFormat='%(asctime)s %(levelname)s %(message)s'

logLevel= logging.DEBUG

logMode = 'w'



logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)



logging.debug("Debug message")

logging.info("Informative message")

logging.error("Error message")

logging.warning('Protocol problem: %s', 'connection reset')

'''
import logging
import os
import datetime

logFile = 'recorregut.log'
logFormat='%(asctime)s %(levelname)s %(message)s'
logLevel= logging.DEBUG
logMode = 'at'

logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)

def recorrer_arbol_directorios(directorio):
    try:
        # Obtener la lista de archivos y directorios en el directorio actual
        contenido = os.listdir(directorio)
        # Recorrer cada elemento del directorio actual
        for elemento in contenido:
            # Crear la ruta completa del elemento
            ruta_elemento = os.path.join(directorio, elemento)
            # Si el elemento es un directorio, recorrer recursivamente
            if os.path.isdir(ruta_elemento):
                print("Directorio:", ruta_elemento)
                recorrer_arbol_directorios(ruta_elemento)
            else:
                print("Archivo:", ruta_elemento)
    except Exception as e:
        log_error(str(e))

def log_error(error):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("recorregut.log", mode='at', encoding='utf-8') as file:
        file.write(f"{fecha_hora} - {error}\n")
    print(f"Error: {error}")
    return error
# Función principal
# todos los errores se guardan en el archivo recorregut.log, incluso si el directlrui no existe
def main():
    # Solicitar al usuario el directorio inicial
    directorio_inicial = input("Introduce la ruta del directorio inicial: ")
    # Verificar si el directorio ingresado existe i guardar el error en el log
    if not os.path.isdir(directorio_inicial):
        logging.error("El directorio especificado no existe.")
    else:
        # Llamar a la función recursiva para recorrer el árbol de directorios
        print("\nRecorrido del árbol de directorios:")
        recorrer_arbol_directorios(directorio_inicial)

if __name__ == "__main__":
    main()
    log_error("Error de prueba")
    logging.info("Informative message")
    logging.error("Error message")
    logging.warning('Protocol problem: %s', 'connection reset')
    logging.debug("Debug message")




