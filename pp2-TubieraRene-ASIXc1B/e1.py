'''
Rene Tubiera Sadinas
M03
UF1 A4 Prova Practica 2
14/12/23
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