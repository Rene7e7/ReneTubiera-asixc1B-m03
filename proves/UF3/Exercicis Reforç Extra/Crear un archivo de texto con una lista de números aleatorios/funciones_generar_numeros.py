import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):
    try:
        with open("numeros_aleatorios.txt", "w") as f:
            for _ in range(cantidad):
                numero = random.randint(minimo, maximo)
                f.write(f"{numero}\n")
    except OSError:
        print("Error al generar los números aleatorios.")
