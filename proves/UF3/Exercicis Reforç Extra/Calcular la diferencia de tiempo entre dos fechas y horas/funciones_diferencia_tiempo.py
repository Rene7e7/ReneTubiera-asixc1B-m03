import datetime

def calcular_diferencia_tiempo(fecha_hora1, fecha_hora2):
    try:
        fecha_hora1 = datetime.datetime.strptime(fecha_hora1, "%Y-%m-%d %H:%M:%S")
        fecha_hora2 = datetime.datetime.strptime(fecha_hora2, "%Y-%m-%d %H:%M:%S")
        diferencia = fecha_hora2 - fecha_hora1
        return diferencia
    except ValueError:
        print("Formato de fecha y hora incorrecto.")
        return datetime.timedelta(0)
