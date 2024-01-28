'''
e16.py
Una empresa paga als seus empleats amb base en les hores treballades a la setmana. Escriu un programa que:
demani per teclat el nombre de treballadors de l’empresa i el sou per hora treballada
demani per cada treballador:
el nombre d’hores treballada a la setmana
mostri per pantalla el sou setmanal del treballador
mostri el total corresponent als sous pagats per l’empresa en una setmana

'''

try:
    # Solicitar el número de trabajadores en la empresa
    Treballadors_empresa = int(input("Quants treballadors hi ha a la empresa? "))
    sou_pagats_setmanal = 0  # Inicializar el total de salarios pagados semanalmente

    # Iterar sobre cada trabajador
    for treballador in range(1, Treballadors_empresa + 1):
        # Solicitar el salario por hora del trabajador
        sou_per_hora = float(input(f"Quin és el sou per hora treballada del treballador {treballador}? "))
        # Solicitar el número de horas trabajadas por el trabajador
        hores_treballades = float(input(f"Quantes hores treballa el treballador {treballador}? "))

        # Calcular el salario semanal del trabajador
        sou_setmanal_treballador = hores_treballades * sou_per_hora
        # Acumular el salario semanal al total de salarios pagados
        sou_pagats_setmanal += sou_setmanal_treballador

        print(f"Sou Setmanal del {treballador} Treballador es {sou_setmanal_treballador} ")
        print(f"Sou pagat Total de l'empresa: {sou_pagats_setmanal}")
        print(f"El {treballador} Treballador, el seu sou per hora es {sou_per_hora}")
        print("--------------------------------------------------------------------")

except ValueError:
    # Capturar errores si los datos ingresados no son números válidos
    print("Error: Introdueix nombres vàlids (sencer o decimal) per les hores i el salari.")




