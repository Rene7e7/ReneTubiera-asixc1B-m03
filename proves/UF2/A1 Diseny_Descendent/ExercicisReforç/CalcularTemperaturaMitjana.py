'''
Creeu una funció, calcularTemperaturaMitjana, que calculi la temperatura mitjana d'un dia a partir de la seva
temperatura màxima i mínima. Escriu un programa principal, que utilitzant la funció anterior, vagi demanant la
temperatura màxima i mínima de cada dia i vaja mostrant la mitjana. Abans de tot, el programa demanarà el nombre
de dies que s'introduiran.
Les temperatures màximes, mínimes i mitjanes podran tenir decimals.

'''

def calcularTemperaturaMitjana(maxima, minima):
    return (maxima + minima) / 2

def main():
    dies = int(input("Introdueix el nombre de dies: "))
    for i in range(dies):
        maxima = float(input("Introdueix la temperatura màxima: "))
        minima = float(input("Introdueix la temperatura mínima: "))
        print(f"La temperatura mitjana és {calcularTemperaturaMitjana(maxima, minima)}")

if __name__ == "__main__":
    main()

