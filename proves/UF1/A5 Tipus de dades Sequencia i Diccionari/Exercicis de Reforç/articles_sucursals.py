'''
e14.py
Crear un programa que llegeixi els preus de 5 articles i les quantitats venudes per una empresa a les seves 3 sucursals. El programa demanarà per teclat:
Els preus de cada article
La quantitat de cada article venut a cada sucursal
A partir de les dades anteriors el programa calcularà i mostrarà per pantalla:
Per cada article, quantes unitats s'han venut en total
La quantitat d'articles venuts a la sucursal 2
La quantitat de l'article 3 venut a la sucursal 1
La recaptació total de cada sucursal
La recaptació total de l’empresa
La sucursal de més recaptació
Pista: podeu fer servir les funcions sum i max de Python.

'''
# Inicializar las listas de las sucursales
sucursal1 = []
sucursal2 = []
sucursal3 = []
recapitulacion_total = 0

for _ in range(5):
    article = input("Nombre del artículo: ")
    precio = float(input(f"Precio del artículo {article}: "))
    cantidad_sucursal1 = int(input(f"Cantidad vendida en Sucursal 1 para {article}: "))
    cantidad_sucursal2 = int(input(f"Cantidad vendida en Sucursal 2 para {article}: "))
    cantidad_sucursal3 = int(input(f"Cantidad vendida en Sucursal 3 para {article}: "))

    # Almacenar las ventas en cada sucursal
    sucursal1.append(precio * cantidad_sucursal1)
    sucursal2.append(precio * cantidad_sucursal2)
    sucursal3.append(precio * cantidad_sucursal3)

    # Calcular la recapitulación total de la empresa
    recapitulacion_total += precio * (cantidad_sucursal1 + cantidad_sucursal2 + cantidad_sucursal3)

# Calcular y mostrar los resultados
print("\nResultados:")
print("------------")

# Por cada artículo, cuántas unidades se han vendido en total
for i, total in enumerate([sum(sucursal1), sum(sucursal2), sum(sucursal3)], start=1):
    print(f"Total de unidades vendidas en Sucursal {i}: {total}")

# La cantidad de artículos vendidos en la sucursal 2
print(f"\nTotal de artículos vendidos en la Sucursal 2: {sum(sucursal2)}")

# La cantidad del artículo 3 vendido en la sucursal 1
print(f"\nCantidad del Artículo 3 vendido en la Sucursal 1: {sucursal1[2]}")

# La recapitulación total de cada sucursal
print(f"\nRecapitulación total de la Sucursal 1: {sum(sucursal1)}")
print(f"Recapitulación total de la Sucursal 2: {sum(sucursal2)}")
print(f"Recapitulación total de la Sucursal 3: {sum(sucursal3)}")

# La recapitulación total de la empresa
print(f"\nRecapitulación total de la empresa: {recapitulacion_total}")

# La sucursal de más recaptación
sucursales = ["Sucursal 1", "Sucursal 2", "Sucursal 3"]
recaps = [sum(sucursal1), sum(sucursal2), sum(sucursal3)]
sucursal_mas_recaptacion = sucursales[recaps.index(max(recaps))]
print(f"\nSucursal con más recaptación: {sucursal_mas_recaptacion}")


