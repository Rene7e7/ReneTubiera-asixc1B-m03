import datetime
import os

def iniciar_programa():
    """Registra el inicio del programa en el archivo de log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join("log", "boges.log"), 'a', encoding='utf-8') as file:
        file.write("[{}] Inicio del programa\n".format(timestamp))

def finalizar_programa():
    """Registra el final del programa en el archivo de log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join("log", "boges.log"), 'a', encoding='utf-8') as file:
        file.write("[{}] Fin del programa\n".format(timestamp))

def registrar_error(error):
    """Registra un error en el archivo de log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join("log", "boges.log"), 'a', encoding='utf-8') as file:
        file.write("[{}] ERROR: {}\n".format(timestamp, error))

def log(mensaje):
    """Registra un mensaje en el archivo de log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join("log", "boges.log"), 'a', encoding='utf-8') as file:
        file.write("[{}] {}\n".format(timestamp, mensaje))
