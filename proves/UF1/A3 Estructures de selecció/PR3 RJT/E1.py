"""
Rene Tubiera
Jordi Yu
Taranpreet Kaur
8/11/2023
UF1 Pr3
e1.  isBigger.py
Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia.
I torna a mostrar els valors per pantalla
"""
#Usaremos una variable temporal donde haremos el intercambio
Num1 = int(input("Ponga un el primer numero: "))
Num2 = int(input("Ponga un el segundo numero: "))
if Num1 >= Num2:
    Num3 = Num1
    Num1 = Num2
    Num2 = Num3
    print("El numero 1 es:", Num1)
    print("El numero 2 es: ", Num2)
else:
    print("El numero 1 es:", Num1)
    print("El numero 2 es: ", Num2)
