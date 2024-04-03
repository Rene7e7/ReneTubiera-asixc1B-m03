'''
Escriure dues funcions que permetin calcular:
La quantitat de segons en un temps donat en hores, minuts i segons.
La quantitat d'hores, minuts i segons d'un temps donat en segons.
Escriu un programa principal amb un menú on es pot triar l'opció de convertir segons, convertir hores, minuts i
segons o sortir del programa.

'''

def segonsEnTemps(hores, minuts, segons):
    return hores * 3600 + minuts * 60 + segons

def tempsEnSegons(segons):
    hores = segons // 3600
    minuts = segons % 3600 // 60
    segons = segons % 60
    return hores, minuts, segons

def main():
    while True:
        print("1. Convertir segons a temps")
        print("2. Convertir temps a segons")
        print("3. Sortir")
        opcio = int(input("Escull una opció: "))
        if opcio == 1:
            hores = int(input("Introdueix les hores: "))
            minuts = int(input("Introdueix els minuts: "))
            segons = int(input("Introdueix els segons: "))
            print(f"El temps en segons és {segonsEnTemps(hores, minuts, segons)}")
        elif opcio == 2:
            segons = int(input("Introdueix els segons: "))
            print(f"El temps és {tempsEnSegons(segons)}")
        elif opcio == 3:
            break
        else:
            print("Opció incorrecta")

if __name__ == "__main__":
    main()
