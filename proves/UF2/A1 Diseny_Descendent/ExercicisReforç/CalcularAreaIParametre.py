'''
Dissenyeu dues funcions, calcularArea i calcularPerimetre, que calculin respectivament l'àrea i el perímetre d'una
circumferència. Les funcions reben un paràmetre, radi, que és un nombre que pot tenir decimals.
Utilitza aquesta funció en un programa que llegeixi el radi d'una circumferència i en mostri l'àrea i el perímetre.

'''

def calcularArea(radi):
    return 3.1416 * radi ** 2

def calcularPerimetre(radi):
    return 2 * 3.1416 * radi

def main():
    radi = float(input("Introdueix el radi de la circumferència: "))
    print(f"Àrea: {calcularArea(radi)}")
    print(f"Perímetre: {calcularPerimetre(radi)}")

if __name__ == "__main__":
    main()

    
