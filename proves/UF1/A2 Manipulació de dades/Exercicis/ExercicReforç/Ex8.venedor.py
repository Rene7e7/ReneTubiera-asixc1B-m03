"""
Un venedor percep cada mes un sou base més un 10% de l'import de cada venda realitzada al mes en concepte de comissió de vendes.

Realitza un programa que a partir d'un import de sou base i l'import de tres vendes, calculi i escriu en pantalla:

l'import percebut en concepte de comissió de vendes
l'import total percebut pel venedor (el salari)

Nota: els imports de salari base i de les tres vendes seran entrats per teclat.

"""

# Pedir al usuario el salario base del vendedor
salario_base = float(input("Introduce el salario base del vendedor: "))

# Pedir al usuario el importe de las tres ventas
venta1 = float(input("Introduce el importe de la primera venta: "))
venta2 = float(input("Introduce el importe de la segunda venta: "))
venta3 = float(input("Introduce el importe de la tercera venta: "))

# Calcular la comisión de ventas (10% de la suma de las ventas)
comision_ventas = (venta1 + venta2 + venta3) * 0.10

# Calcular el salario total
salario_total = salario_base + comision_ventas

# Mostrar los resultados
print(f"La comisión de ventas es: {comision_ventas:.2f}")
print(f"El salario total del vendedor es: {salario_total:.2f}")
