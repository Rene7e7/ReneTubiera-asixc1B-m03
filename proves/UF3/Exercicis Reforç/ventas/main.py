import ventas

def main():
    ventas.crear_directoris()
    registro = ventas.llegir_registro("registre_ventes.txt")

    print("1. Registrar venta")
    print("2. Calcular total de ventas")
    print("3. Guardar y salir")
    opcio = input("Escoge una opción: ")

    while opcio != "3":
        if opcio == "1":
            producto = input("Producto vendido: ")
            cantidad = int(input("Cantidad vendida: "))
            precio = float(input("Precio unitario: "))
            ventas.registrar_venta(registro, producto, cantidad, precio)
        elif opcio == "2":
            print(f"Total de ventas: {ventas.calcular_total(registro)}")
        opcio = input("Escoge una opción: ")

    ventas.guardar_registro("registre_ventes.txt", registro)

if __name__ == "__main__":
    main()
