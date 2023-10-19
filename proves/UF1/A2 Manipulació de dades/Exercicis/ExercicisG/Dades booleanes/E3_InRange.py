"""
11/10/2023
René Tubiera y Jordi Yu

E3. InRange
Escriu un programa que llegeixi 5 enters.
El primer i el segon creen un rang, el tercer i el quart creen un altre rang.
Mostra True si el cinquè valor, està comprès dins els dos rangs, si no False. (Els extrems dels rangs inclosos)
"""

# 5 numeros enters
num1 = int(input("Introdueix el primer numero enter: "))
num2 = int(input("Introdueix el segon numero enter: "))
num3 = int(input("Introdueix el tercer numero enter: "))
num4 = int(input("Introdueix el quart numero enter: "))
num5 = int(input("Introdueix el cinque numero enter: "))

# Comprova si el numero5 esta en el rang entre el numero 1 i 2 , i lo mateix pero entr el numero 3 i 4, si no esta en el rang sera false i si esta en el rang sera True
if num1 <= num5 <= num2 or num3 <= num5 <= num4:
    resultat = True
else:
    resultat = False
print(resultat)