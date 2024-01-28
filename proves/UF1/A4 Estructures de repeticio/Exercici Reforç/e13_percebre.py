'''
e13.py
Una empresa vol enregistrar el nombre d’hores que treballa diàriament un empleat
durant la setmana (sis dies laborals) i determinar-ne el total d’hores treballades,
així com el sou que rebrà per aquestes.
Escriu el programa que permet calcular aquestes dades. En concret, el programa:
demanarà per teclat el sou per hora
per cadascú dels 6 dies, demanarà quantes hores s’ha treballat
mostrarà el total d’hores treballades i el sou total a percebre

'''
try:
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
        if 0 < hores_treball <= 12:
            # Mostrar información del día
            print(f"DIA: {dia}")
            print(f"En este día he treballat {hores_treball} hores.")

            # Actualizar totales
            hores_treball_total += hores_treball
            sou_Total += sou

            print(f"Hores total d'aquesta setmana: {hores_treball_total}")
            print(f"Sou total a percebre: {sou_Total}")
        else:
            print("Incorrecto: Las horas deben ser mayores que 0 y no más de 12.")
            # Pedir nuevamente las horas trabajadas
            hores_treball = int(input(f"Digam cuantas hores treballas en el dia {dia}: "))
except ValueError:
    print("Error")
