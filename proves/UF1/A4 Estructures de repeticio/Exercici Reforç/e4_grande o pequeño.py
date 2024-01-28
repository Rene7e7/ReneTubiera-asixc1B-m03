'''
e4.py
Implementa un programa que demani números per teclat.  Prèviament, el programa ha de demanar la quantitat de números que l’usuari vol introduir.
Un cop introduïts tots els números, el programa informarà de quants són més grans que 0, menors que 0 i iguals a 0.

'''

try:
    cantidad_num = int(input("Dime un numero para la cantidad: "))

    # Inicializar listas y contador
    num_grande = []  # Lista para almacenar números mayores a 0
    num_pequeño = []  # Lista para almacenar números menores a 0
    num_zero = 0  # Contador para números iguales a 0

    for i in range(cantidad_num):
        numero = int(input("Dime un numero: "))

        if numero > 0:
            num_grande.append(numero)  # Agregar el número a la lista de números grandes
        elif numero < 0:
            num_pequeño.append(numero)  # Agregar el número a la lista de números pequeños
        elif numero == 0:
            num_zero += 1  # Incrementar el contador de números iguales a 0

    # Imprimir resultados
    print(f"Números mayores a 0: {num_grande}")
    print(f"Números menores a 0: {num_pequeño}")
    print(f"Números iguales a 0: {num_zero}")

except ValueError:
    print("Error: Debes ingresar números enteros.")


