import datetime

def registrar_evento(evento):
    fecha_hora_actual = datetime.datetime.now()
    try:
        with open("registro_eventos.txt", "a") as f:
            f.write(f"{fecha_hora_actual} - {evento}\n")
    except OSError:
        print("Error al registrar el evento.")
