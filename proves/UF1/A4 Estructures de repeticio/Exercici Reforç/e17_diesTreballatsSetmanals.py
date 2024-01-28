'''
e17.py
Fes un programa idèntic al de l’exercici 16 però amb els següents canvis:
per cada treballador es demanarà el nombre de dies que ha treballat
en lloc de demanar el nombre d’hores setmanal treballat per treballador, es demanarà el nombre d’hores treballats diaris per cada dia treballat del treballador
Amb les modificacions anteriors, el nou programa ha de mostrar igualment per pantalla el sou setmanal de cada treballador i el sou setmanal pagat al total dels treballadors.

'''

try:
    # Solicitar el número de trabajadores en la empresa
    Treballadors_empresa = int(input("Quants treballadors hi ha a la empresa? "))
    sou_pagats_setmanal = 0  # Inicializar el total de salarios pagados semanalmente

    # Iterar sobre cada trabajador
    for treballador in range(1, Treballadors_empresa + 1):
        # Solicitar el salario por hora del trabajador
        sou_per_hora = float(input(f"Quin és el sou per hora treballada del treballador {treballador}? "))
        # Solicitar el número de días que ha trabajado el trabajador
        dies_treballats = int(input(f"Quants dies ha treballat el treballador {treballador}? "))

        # Inicializar el salario semanal del trabajador
        sou_setmanal_treballador = 0

        # Iterar sobre cada día trabajado y solicitar las horas trabajadas
        for dia in range(1, dies_treballats + 1):
            hores_diaries = float(input(f"Quantes hores treballades té el treballador {treballador} el dia {dia}? "))
            sou_setmanal_treballador += hores_diaries * sou_per_hora

        # Acumular el salario semanal al total de salarios pagados
        sou_pagats_setmanal += sou_setmanal_treballador

        # Mostrar el salario semanal del trabajador actual
        print(f"Sou Setmanal del treballador {treballador}: {sou_setmanal_treballador:.2f}")
        print("--------------------------------------------------------------------")

    # Mostrar el salario total pagado por la empresa en una semana
    print(f"Sou pagat Total de l'empresa: {sou_pagats_setmanal:.2f}")

except ValueError:
    # Capturar errores si los datos ingresados no son números válidos
    print("Error: Introdueix nombres vàlids (sencer o decimal) per les hores i el salari.")
