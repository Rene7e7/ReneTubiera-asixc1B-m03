def sumar_numeros(archivo):
    suma = 0
    try:
        with open(archivo, "r") as f:
            for linea in f:
                suma += int(linea.strip())
        return suma
    except FileNotFoundError:
        print("El archivo no existe.")
        return 0
