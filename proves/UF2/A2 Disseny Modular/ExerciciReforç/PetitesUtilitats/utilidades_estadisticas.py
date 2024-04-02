def calcular_media(datos):
    if not datos:
        raise ValueError("La lista de datos está vacía")
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    if not datos:
        raise ValueError("La lista de datos está vacía")
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        return (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        return datos_ordenados[n//2]

def calcular_desviacion_estandar(datos):
    if not datos:
        raise ValueError("La lista de datos está vacía")
    media = calcular_media(datos)
    n = len(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    return (suma_cuadrados / n) ** 0.5

def menu_estadisticas():
    while True:
        print("\nMenu d'Utilitats Estadístiques:")
        print("1.1 - Calcular mitjana")
        print("1.2 - Calcular mediana")
        print("1.3 - Calcular desviació estàndard")
        print("1.4 - Tornar al menú anterior")

        opcion = input("Selecciona una opció: ")

        if opcion == "1.1":
            try:
                datos = [float(x) for x in input("Introdueix els nombres separats per espai: ").split()]
                print("La mitjana és:", calcular_media(datos))
            except ValueError:
                print("Error: Introdueix nombres vàlids.")
        elif opcion == "1.2":
            try:
                datos = [float(x) for x in input("Introdueix els nombres separats per espai: ").split()]
                print("La mediana és:", calcular_mediana(datos))
            except ValueError:
                print("Error: Introdueix nombres vàlids.")
        elif opcion == "1.3":
            try:
                datos = [float(x) for x in input("Introdueix els nombres separats per espai: ").split()]
                print("La desviació estàndard és:", calcular_desviacion_estandar(datos))
            except ValueError:
                print("Error: Introdueix nombres vàlids.")
        elif opcion == "1.4":
            break
        else:
            print("Opció no vàlida, si us plau, tria una opció vàlida.")
