import math

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_primeros_primos(n):
    numeros_primos = []
    i = 2
    while len(numeros_primos) < n:
        if es_primo(i):
            numeros_primos.append(i)
        i += 1

    print(f"Los primeros {n} números primos son: {numeros_primos}")

if __name__ == "__main__":
    try:
        cantidad_primos = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
        mostrar_primeros_primos(cantidad_primos)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
