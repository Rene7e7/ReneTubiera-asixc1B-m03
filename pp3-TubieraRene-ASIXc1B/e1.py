'''
Rene Tubiera Sadinas
1/02/2024
ASIXc1B
UF1 A5
Prova Practica 3
'''

llista_paraules = []
contador_paraules = 0
contador_lletras = 0
try:
    for i in range(1000000):
        # El programa ens demana paraules
        paraula = str(input("Digam 10000000 paraules: "))
        # Guarda les paraules en la llista de paraules
        llista_paraules.append(paraula)
        # Em compta les paraules que posem a la llista
        contador_paraules += 1

        # Tambe ens contara numeros de lletras que hi ha en la llista
        contador_lletras += len(paraula)

        # Compte les lletres que te la paraule que printem
        print(len(paraula))

        # Mostra la llista de paraules
        print(llista_paraules)

        # Si posem \q, acaba el programa
        if paraula == "\q":
            break
    # Ens printa la paraula mes llarga
    print("La paraula mes llarga es", len(max(llista_paraules)))
    # Ens printa la paraula mes curta
    print("La paraula mes curta es", len(min(llista_paraules)))
    # Ens Calcula la mitajan de la llista de paraules
    print("La mitjana de la llista de paraules es:", contador_paraules/2)
# Donara Error perque hem posat un numero, i en aquest programa no es pot posar numeros
except ValueError:
    print("Error, no s'accepta numeros en aquest programa")


