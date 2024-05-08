import funciones_diferencia_tiempo as fdt

def main():
    fecha_hora1 = input("Introduce la primera fecha y hora (YYYY-MM-DD HH:MM:SS): ")
    fecha_hora2 = input("Introduce la segunda fecha y hora (YYYY-MM-DD HH:MM:SS): ")
    diferencia = fdt.calcular_diferencia_tiempo(fecha_hora1, fecha_hora2)
    print(f"La diferencia de tiempo es de {diferencia}")

if __name__ == "__main__":
    main()
