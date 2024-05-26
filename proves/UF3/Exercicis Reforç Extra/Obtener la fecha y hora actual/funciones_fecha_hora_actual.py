import datetime

def obtener_fecha_hora_actual():
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return fecha_hora_actual
