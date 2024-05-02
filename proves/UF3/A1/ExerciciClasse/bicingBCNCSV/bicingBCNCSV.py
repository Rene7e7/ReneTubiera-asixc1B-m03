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

# region capacity
def capacity(nomarxiu):
    dades = pd.read_csv(nomarxiu)
    estacio_max_bicis = dades['capacity'].idxmax()
    max_bicis = dades.loc[estacio_max_bicis, 'capacity']
    estacio_min_bicis = dades['capacity'].idxmin()
    min_bicis = dades.loc[estacio_min_bicis, 'capacity']
    total_capacity = dades['capacity'].sum()
    total_capacity = dades.drop_duplicates(subset='station_id')['capacity'].sum()
    return estacio_max_bicis, estacio_min_bicis, total_capacity

nomarxiu = '2023_03_Marc_BicingNou_INFORMACIO.csv'
estacio_max_bicis, estacio_min_bicis, total_capacity = capacity(nomarxiu)
print(f'Estació amb més bicicletes: {estacio_max_bicis}')
print(f'Estació amb menys bicicletes: {estacio_min_bicis}')
print(f'Capacity total de la ciutat de Barcelona: {total_capacity}')

capacity('2023_03_Marc_BicingNou_INFORMACIO.csv')
# endregion


