contI = 1  # Inicialización de contador para el primer factor
contJ = 1  # Inicialización de contador para el segundo factor

# Bucle externo para el primer factor (contI)
while contI <= 10:
    # Bucle interno para el segundo factor (contJ)
    while contJ <= 10:
        # Imprime la multiplicación de contI y contJ
        print("%d x %d = %d" % (contI, contJ, contI * contJ))

        # Incrementa el contador del segundo factor
        contJ += 1

    # Reinicia el contador del segundo factor para la siguiente fila
    contJ = 1

    # Incrementa el contador del primer factor para pasar a la siguiente fila
    contI = contI + 1

    # Imprime una línea divisoria entre cada
    print("--------------")
