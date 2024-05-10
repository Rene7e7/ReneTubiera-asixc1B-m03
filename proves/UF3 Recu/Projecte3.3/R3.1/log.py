import datetime

def registrar_error(error):
    """Registra un error en el archivo de log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("boges.log", 'a', encoding='utf-8') as file:
        file.write("[{}] ERROR: {}\n".format(timestamp, error))

def log(mensaje):
    """Registra un mensaje en el archivo de log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("boges.log", 'a', encoding='utf-8') as file:
        file.write("[{}] {}\n".format(timestamp, mensaje))
