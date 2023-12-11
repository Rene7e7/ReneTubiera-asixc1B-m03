"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
e3. Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
 Ex: 	si el límit és 31 sumaParells 240 i sumaSenars 225
si el límit és 54 sumaParells 702 i sumaSenars 729
"""
# Inicialización de variables para la suma de números pares e impares
parell = 0
imparell = 0

try:
    # Solicita al usuario que ingrese el límite superior
    num = int(input("Dime número límite: "))

    # Bucle para la suma de números pares (comienza desde 0, salta de 2 en 2)
    for i in range(0, num + 1, 2):
        parell += i

    # Bucle para la suma de números impares (comienza desde 1, salta de 2 en 2)
    for j in range(1, num + 1, 2):
        imparell += j

    # Imprime el resultado
    print("Si el límite es", num, "sumaParells es", parell, "y sumaSenar es", imparell)

except ValueError:
    # Captura el error si la entrada no es un número entero
    print("Error: Debes ingresar un número entero.")

except Exception as e:
    # Captura cualquier otro tipo de error e imprime un mensaje general de error
    print("Error:", e)

