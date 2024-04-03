'''
Escriu un programa que demani dos números sencers a l'usuari i digui si algun és múltiple de l'altre.
Crea una funció esMultiple que rebi els dos números, i torna un booleà que indica si el primer és múltiple del segon.

'''

def esMultiple(num1, num2):
    return num1 % num2 == 0 or num2 % num1 == 0

def main():
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    if esMultiple(num1, num2):
        print("Un dels números és múltiple de l'altre")
    else:
        print("Cap dels números és múltiple de l'altre")

if __name__ == "__main__":
    main()

