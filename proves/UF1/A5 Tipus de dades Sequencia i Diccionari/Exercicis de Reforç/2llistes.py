'''

e7.py
Escriu un programa que declari tres llistes “llista1”, “llista2” i “llista3”, amb cinc sencers cadascuna, i que demani valors per a “llista1” i “llista2”. El programa ha d'emplenar llavors llista3 de manera que contingui la suma dels elements de ‘llista1’ i ‘llista2’.
Per exemple, donades aquestes llistes:
llista1 = [23,54,-12,0,70]
llista2 = [543,-234,5,11,20]
‘llista3’ ha de tenir aquests elements:
llista3 = [566,-180,-7,11,90]

'''

# Declara les llistes llista1 i llista2
llista1 = []
llista2 = []

# Demana valors per a llista1
print("Introdueix valors per a llista1:")
for i in range(5):
    valor = int(input(f"Element {i + 1}: "))
    llista1.append(valor)

# Demana valors per a llista2
print("Introdueix valors per a llista2:")
for i in range(5):
    valor = int(input(f"Element {i + 1}: "))
    llista2.append(valor)

# Inicialitza llista3 amb la suma dels elements de llista1 i llista2 sense usar zip
llista3 = []
for i in range(5):
    suma = llista1[i] + llista2[i]
    llista3.append(suma)

# Mostra les llistes originals i la llista resultant
print(f"\nllista1 = {llista1}")
print(f"llista2 = {llista2}")
print(f"llista3 = {llista3}")
