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

        # Mostrar el salario semanal del trabajador actual
        print(f"Sou Setmanal del treballador {treballador}: {sou_setmanal_treballador:.2f}")

    # Mostrar el salario total pagado por la empresa en una semana
    print(f"Sou pagat Total de l'empresa: {sou_pagats_setmanal:.2f}")

except ValueError:
    # Capturar errores si los datos ingresados no son números válidos
    print("Error: Introdueix nombres vàlids (sencer o decimal) per les hores i el salari.")
