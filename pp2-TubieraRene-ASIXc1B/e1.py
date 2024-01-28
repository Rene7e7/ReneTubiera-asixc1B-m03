'''
Rene Tubiera Sadinas
M03
UF1 A4 Prova Practica 2
14/12/23
'''

try:
    # Demana a l'usuari un numero
    numero = abs(int(input("Digam un numero: ")))
    numero_original = numero
    cont = 1
    while numero // 10 != 0:
        numero = numero // 10
        cont = cont+1

    print(f"El Numero {numero} te {cont} digits")
# Ens sortira un missatge si l'usuari no psa un numero
except ValueError:
    print("No es un numero")

'''

try:
    # Demana a l'usuari un numero
    numero = int(input("Digam un numero: "))
    # Variable que fa un range al 0 al 9
    digits = range(0,9)
    # Variable per l aquntitat de digits que te le numero
    quantitat_digits = 0

    # mentre que el numero no sigui menor que 0
    while numero < 0:
        # Si el numero que ha demanat te el digits
        if numero == digits:
            quantitat_digits += 1
        print(f"El numero té {numero} digits ")
# Ens sortira un missatge si l'usuari no psa un numero
except ValueError:
    print("No es un numero")

'''
try:
    # Demana a l'usuari un numero
    numero = int(input("Digam un numero: "))
    # Variable que fa un range del 0 al 9
    digits = range(0, 10)
    # Variable per la quantitat de digits que té el numero
    quantitat_digits = 0

    # mentre que el numero no sigui menor que 0
    while numero > 0:
        # Si el ultim digit del numero està dins de la llista digits
        ultim_digit = numero % 10
        if ultim_digit in digits:
            quantitat_digits += 1
        # Elimina l'últim dígit del número
        numero = numero // 10

    print(f"El numero té {quantitat_digits} digits amb digits entre 0 i 9.")
# Ens sortirà un missatge

'''
    
'''
