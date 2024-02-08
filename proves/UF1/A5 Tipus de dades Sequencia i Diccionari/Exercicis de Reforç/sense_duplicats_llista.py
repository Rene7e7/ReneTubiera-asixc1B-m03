'''
e17.py
Crear un programa que afegeix números a una llista fins que introduïm un número negatiu. A continuació heu de crear i mostrar per pantalla una nova llista igual que l'anterior, però on s'han eliminat els números duplicats.
'''

# Inicializar la lista
llista_original = []

# Afegir números a la llista fins que s'introdueixi un número negatiu
while True:
    numero = int(input("Introdueix un número (negatiu per sortir): "))
    if numero < 0:
        break
    llista_original.append(numero)

# Mostrar la llista original
print("Llista original:", llista_original)

# Crear una nova llista sense números duplicats
llista_sense_duplicats = list(set(llista_original))

# Mostrar la nova llista
print("Nova llista sense números duplicats:", llista_sense_duplicats)
