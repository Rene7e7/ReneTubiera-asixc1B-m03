# Precio por hora
sou = 2000

# Inicializar variables
sou_Total = 0
hores_treball_total = 0

# Bucle para cada día de la semana
for dia in range(1, 7):
    # Solicitar las horas trabajadas
    hores_treball = int(input(f"Digam cuantas hores treballas en el dia {dia}: "))

    # Verificar si las horas trabajadas son válidas (mayor que 0 y no más de 24)
    if 0 < hores_treball <= 24:
        # Mostrar información del día
        print(f"DIA: {dia}")
        print(f"En este día he treballat {hores_treball} hores.")

        # Actualizar totales
        hores_treball_total += hores_treball
        sou_Total += hores_treball * sou

        print(f"Hores total d'aquesta setmana: {hores_treball_total}")
        print(f"Sou total a percebre: {sou_Total}")
    else:
        print("Incorrecto: Las horas deben ser mayores que 0 y no más de 24.")
        # Pedir nuevamente las horas trabajadas
        hores_treball = int(input(f"Digam cuantas hores treballas en el dia {dia}: "))
