'''
Crea dues funcions calcularMax i calcularMin. Cadascuna rep una llista amb valors enters i torna,
respectivament el valor màxim i el mínim de la llista.
Nota: no es poden fer servir la funció “min”, ni “max” de Python.
Escriu un programa que demani números per teclat i mostri el màxim i el mínim, utilitzant les
funcions anteriors. Abans de res, el programa demanarà el nombre de números a entrar.

'''
def calcularMax(llista):
    max = llista[0]
    for i in llista:
        if i > max:
            max = i
    return max

def calcularMin(llista):
    min = llista[0]
    for i in llista:
        if i < min:
            min = i
    return min

def main():
    llista = []
    n = int(input("Introdueix el nombre de números: "))
    for i in range(n):
        llista.append(int(input("Introdueix un número: ")))

    print(f"El màxim és {calcularMax(llista)}")
    print(f"El mínim és {calcularMin(llista)}")

if __name__ == "__main__":
    main()
