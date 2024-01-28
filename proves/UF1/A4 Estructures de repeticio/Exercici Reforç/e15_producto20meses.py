'''
e15.py
Una persona va adquirir un producte per pagar en 20 mesos.
El primer mes va pagar 10€, el segon 20€, el tercer 40€ i així successivament
(cada mes va pagar el doble que a l’anterior) Realitzar un algorisme que mostri quant ha de
pagar mensualment i el total del qual ha de pagar després dels 20 mesos.

'''

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
