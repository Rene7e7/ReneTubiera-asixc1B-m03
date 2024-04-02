def is_palindrome(frase):
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]

def cifrado_cesar(texto, clave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - offset + clave) % 26 + offset)
        else:
            resultado += char
    return resultado

def menu_cadenas():
    while True:
        print("\nMenu d'Utilitats de Cadenes:")
        print("2.1 - Crazy Words")
        print("2.2 - És una frase palindroma?")
        print("2.3 - Xifratge de Cèsar")
        print("2.4 - Tornar al menú anterior")

        opcion = input("Selecciona una opció: ")

        if opcion == "2.1":
            print("Funcionalitat no implementada.")
        elif opcion == "2.2":
            frase = input("Introdueix una frase: ")
            if is_palindrome(frase):
                print("La frase és un palíndrom.")
            else:
                print("La frase no és un palíndrom.")
        elif opcion == "2.3":
            texto = input("Introdueix el text a xifrar: ")
            clave = int(input("Introdueix la clau de xifratge (un nombre enter): "))
            print("Text xifrat:", cifrado_cesar(texto, clave))
        elif opcion == "2.4":
            break
        else:
            print("Opció no vàlida, si us plau, tria una opció vàlida.")
