def generar_informe(inventario):
    informe = "Inventario actualizado:\n"
    for producto, cantidad in inventario.items():
        informe += f"{producto}: {cantidad}\n"
    return informe
