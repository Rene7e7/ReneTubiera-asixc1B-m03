"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
e5. Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes
"""
# Try y except para errores
try:
    resultado = 0
    num1 = int(input("Introduce el primer numero : "))
    num2 = int(input("Introduce el segundo numero : "))
    if num1 < 0 or num2 < 0:
        print("Esta calculadora funciona con solo positivos")
    else:
        for i in range(num2):
            resultado += num1
# Como funciona el rango hasta el limite del numero 2 va sumando las candidades del numero 1
# Por ejemplo si es el 5 x 5: el limite es 5 repite cinco veces suma 5 cada repeticion haciendo resultado: 25
        print("El resultado de",num1," x ",num2, "es: ",resultado)
except ValueError:
    print("ValueError")