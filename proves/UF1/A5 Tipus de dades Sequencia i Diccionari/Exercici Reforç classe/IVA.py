'''
IVA
'''

# Constante del IVA
IVA = 21 / 100

# Lista para almacenar los precios
precios = []

# Obtener los precios de los 10 artículos del usuario
for _ in range(10):
    precio = float(input())
    precios.append(precio)

# Calcular el precio con IVA y mostrar los resultados
for precio in precios:
    precio_con_iva = precio + (precio * IVA)
    print(f'{precio} IVA = {precio_con_iva:.2f}')
