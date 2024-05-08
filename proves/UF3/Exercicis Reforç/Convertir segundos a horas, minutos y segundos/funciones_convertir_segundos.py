import datetime

def convertir_segundos(segundos):
    tiempo = str(datetime.timedelta(seconds=segundos))
    return tiempo
