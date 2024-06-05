def actualizar_inventario(inventario, transacciones):
    for tipo, producto, cantidad in transacciones:
        if tipo == 'venta':
            inventario[producto] -= cantidad
        elif tipo == 'adicion':
            inventario[producto] += cantidad
    return inventario
