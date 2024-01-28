from time import sleep

segundos = 00
minutos = 59
horas = 23
while True:
    print(f'{horas}:{minutos:}:{segundos}')
    segundos +=1
    sleep(0.03)
    if segundos == 60:
        minutos +=1
        segundos = 0
        sleep(1)
    elif minutos == 60:
        minutos =0
        horas+=1
    elif horas == 24:
        horas = 0
        minutos = 0
        segundos = 0
