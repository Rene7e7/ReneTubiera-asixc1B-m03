# Inicializar variables
pago_mensual = 10  # Primer pago
total_pagado = 0

# Bucle para los 20 meses
for mes in range(1, 21):
    # Mostrar el pago mensual
    print(f"Mes {mes}: Pagar {pago_mensual}€")

    # Actualizar el total pagado
    total_pagado += pago_mensual

    # Calcular el siguiente pago (el doble del mes anterior)
    pago_mensual *= 2

# Mostrar el total pagado después de 20 meses
print(f"\nTotal pagado después de 20 meses: {total_pagado}€")
