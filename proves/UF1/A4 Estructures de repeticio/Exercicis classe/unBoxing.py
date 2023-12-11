FUSTA = "🟫"
columna = int(input("Digam una quantitat per a columnas: "))
filas = int(input("Digam una qunatitat per a filas: "))


if columna <= 0 or filas <= 0:
    print("Error")
else:
    for i in range(filas):
        for j in range(columna):
            if i == 0 or i == filas - 1 or j == 0 or j == columna - 1:
                print("🟫", end=" ")
            else:
                print("  ", end=" ")  # Espacios para el interior de la caja
        print()
