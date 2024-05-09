'''
Rene Tubiera Sadinas
4/4/2024
M03 UF2 A1 i A2 pp1B - Prova Practica 1
ASIX1B
'''
def cifrado_cesar(texto, clave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - offset + clave) % 26 + offset)
        else:
            resultado += char
    return resultado

def Utilitat3_1():
    texto = input("Introdueix el text a xifrar: ")
    clave = int(input("Introdueix la clau de xifratge (un nombre enter): "))
    print("Text xifrat:", cifrado_cesar(texto, clave))

Utilitat3_1()
