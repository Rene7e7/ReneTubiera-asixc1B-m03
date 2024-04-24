'''
Fer un programa en Python que llegint el fitxer CSV del Bicing  de Barcelona ens doni la següent informació:

Obtenir la "capacity" de l'estació amb més bicicletes i la que en te menys

Obtenir la "capacity" total de la ciutat de barcelona

Font:  Open Data BCN  Inici >  Ciutat i serveis >  Transport >  Informació de les ...> 2023_03_Marc_BicingNou_INFO ...

Arxiu a processar: 2023_03_Marc_BicingNou_INFORMACIO.csv.7z

quantitat de línies: 4.291.777
'''

import pandas as pd

filename = '2023_03_Marc_BicingNou_INFORMACIO.csv'
# filename = 'bicingBCNCSV.csv'

# region capacity
def capacity():
    dades = pd.read_csv(filename)
    estacio_max = dades['capacity'].idxmax()
    max_bici = dades.loc[estacio_max]
    print("L'estacio amb mes bicicletes es: ")
    print(max_bici)
    estacio_min = dades['capacity'].idxmin()
    min_bici = dades.loc[estacio_min]
    print("L'estacio amb menys bicicletes es: ")
    print(min_bici)
    total_capacity = dades['capacity'].sum()
    print("La capacitat total de la ciutat de Barcelona es: ")
    print(total_capacity)




# endregion
'''
# region total_capacity
def total_capacity():
    reader = csv.DictReader(open(filename))
    total_capacity = 0
    for row in reader:
        total_capacity += int(row['capacity'])
    print("La capacitat total de la ciutat de Barcelona es: ")
    print(total_capacity)
# endregion
'''


capacity()
