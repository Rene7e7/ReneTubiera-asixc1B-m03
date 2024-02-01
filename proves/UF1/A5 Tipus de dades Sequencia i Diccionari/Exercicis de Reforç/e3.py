"""
24/01/2024
Ppr5 UF1
Jordi Yu
Rene Tubiera
e3. Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà traduït a castellà, anglès i klingon.

Exemple
…
print(insults[CAT]) #['Mocos', 'Capsigrany']
print(insults[CAT][0]) #Mocós
print(insults[CAT][1]) #Capsigrany
print(insults[ESP]) #['Mocoso', 'Cabezón']
print(insults[ENG]) #['Brat', 'Stubborn']
print(insults[KLI]) #['Brat', 'Stubborn']

"""
CAT = ("Carallot", "Mocós", "Malparit", "Tros de quòniam")
ESP = ("Tonto","Mocoso","Malparido", "Trozo de algo inútil")
ENG = ("Foolish","Snotty","Cursed","Useless piece")
try:
    insulto = input("Ponga el insulto catalan: ")
    correccion = insulto.capitalize() #para los usuarios que escribe tod0 en mayus o minus
    if correccion in CAT: #si esta en la tupla
        index = CAT.index(correccion) #index funciona selecionando que posicion tiene el objeto de la tupla
        print(f"{correccion},{ESP[index]},{ENG[index]}") #utilizando la misma posicion que los otros
    else:
        print("Error, palabra no encontrada, mire si tienes alguna falta de ortografia")
except:
    print("Error palabra no valida")