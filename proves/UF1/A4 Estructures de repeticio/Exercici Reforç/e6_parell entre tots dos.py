try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    # Asegurarse de que num1 sea menor que num2
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"Números pares entre {num1} y {num2}:")
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i, end=" ")

except ValueError:
    print("Error: Debes ingresar números enteros.")

#WHILE
try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    # Asegurarse de que num1 sea menor que num2
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"Números pares entre {num1} y {num2}:")
    current_num = num1

    while current_num <= num2:
        if current_num % 2 == 0:
            print(current_num, end=" ")
        current_num += 1

except ValueError:
    print("Error: Debes ingresar números enteros.")
