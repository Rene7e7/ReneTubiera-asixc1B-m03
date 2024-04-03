'''
Volem crear un programa que treballi amb fraccions a/b. Per representar una fracció utilitzarem dos sencers: numerador i denominador.
Crearem les funcions següents per treballar amb funcions:
llegirFracció: La tasca d'aquesta funció és llegir per teclat el numerador i el denominador. Quan llegeixis una fracció,
l'has de simplificar.
escriureFracció: Aquesta funció escriu a la pantalla la fracció. Si el dominador és 1, només es mostra el numerador.
calcularMCD: Aquesta funció rep dos nombres i retorna el màxim comú divisor.
simplificarFracció: Aquesta funció simplifica la fracció, per això cal dividir numerador i dominador pel MCD del numerador i denominador.
sumarFraccions: funció que rep dues funcions n1/d1 i n2/d2, i calcula la suma de les dues fraccions. La suma de dues fraccions
és una altra fracció el numerador de la qual=n1*d2+d1*n2 i denominador=d1*d2. Cal simplificar la fracció resultat.
restarFraccions: Funció restant dues fraccions: numerador=n1*d2-d1*n2 i denominador=d1*d2. Cal simplificar la fracció resultat.
multiplicarFraccions: Funció que rep dues fraccions i calcula el producte, per això numerador=n1*n2 i denominador=d1*d2.
Cal simplificar la fracció resultat.
dividirFraccions: Funció que rep dues fraccions i calcula el quocient, per això numerador=n1*d2 i denominador=d1*n2.
Cal simplificar la fracció resultat.
Crear un programa que utilitzant les funcions anteriors mostri el menú següent:
Sumar dues fraccions: En aquesta opció es demanen dues fraccions i es mostra el resultat.
Restar dues fraccions: En aquesta opció es demanen dues fraccions i se'n mostra la resta.
Multiplicar dues fraccions: En aquesta opció es demanen dues fraccions i se'n mostra el producte.
Dividir dues fraccions: En aquesta opció es demanen dues fraccions i se'n mostra el quocient.
Sortir

'''

def llegirFracció():
    numerador = int(input("Introdueix el numerador: "))
    denominador = int(input("Introdueix el denominador: "))
    mcd = calcularMCD(numerador, denominador)
    return numerador // mcd, denominador // mcd

def escriureFracció(numerador, denominador):
    if denominador == 1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")

def calcularMCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def simplificarFracció(numerador, denominador):
    mcd = calcularMCD(numerador, denominador)
    return numerador // mcd, denominador // mcd

def sumarFraccions(n1, d1, n2, d2):
    numerador = n1 * d2 + d1 * n2
    denominador = d1 * d2
    return simplificarFracció(numerador, denominador)

def restarFraccions(n1, d1, n2, d2):
    numerador = n1 * d2 - d1 * n2
    denominador = d1 * d2
    return simplificarFracció(numerador, denominador)

def multiplicarFraccions(n1, d1, n2, d2):
    numerador = n1 * n2
    denominador = d1 * d2
    return simplificarFracció(numerador, denominador)

def dividirFraccions(n1, d1, n2, d2):
    numerador = n1 * d2
    denominador = d1 * n2
    return simplificarFracció(numerador, denominador)

def main():
    while True:
        print("1. Sumar dues fraccions")
        print("2. Restar dues fraccions")
        print("3. Multiplicar dues fraccions")
        print("4. Dividir dues fraccions")
        print("5. Sortir")
        opcio = int(input("Escull una opció: "))
        if opcio == 1:
            n1, d1 = llegirFracció()
            n2, d2 = llegirFracció()
            n, d = sumarFraccions(n1, d1, n2, d2)
            print("La suma és:")
            escriureFracció(n, d)
        elif opcio == 2:
            n1, d1 = llegirFracció()
            n2, d2 = llegirFracció()
            n, d = restarFraccions(n1, d1, n2, d2)
            print("La resta és:")
            escriureFracció(n, d)
        elif opcio == 3:
            n1, d1 = llegirFracció()
            n2, d2 = llegirFracció()
            n, d = multiplicarFraccions(n1, d1, n2, d2)
            print("La multiplicació és:")
            escriureFracció(n, d)
        elif opcio == 4:
            n1, d1 = llegirFracció()
            n2, d2 = llegirFracció()
            n, d = dividirFraccions(n1, d1, n2, d2)
            print("La divisió és:")
            escriureFracció(n, d)
        elif opcio == 5:
            break
        else:
            print("Opció incorrecta")

if __name__ == "__main__":
    main()
    
