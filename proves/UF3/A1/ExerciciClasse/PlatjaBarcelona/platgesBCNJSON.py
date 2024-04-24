'''
Fer un programa en Python que llegint el fitxer JSON de les platges de Barcelona ens doni la següent informació:

Obtenir els noms de tots els districtes de Barcelona que tenen platges CV? i SM?

Obtenir la quantitat de platges que hi ha al districte de "Ciutat Vella"  4?


Font:  Open Data BCN  Inici >  Territori >  Urbanisme i infraestructures >  Platges a la ciutat de ...

Arxiu a processar: opendatabcn_NP-NASIA_Platges-js.json

quantitat de línies:  ???
'''

import json

def district_name():
    with open('opendatabcn_NP-NASIA_Platges-js.json') as x:
        x = json.load(x)
        district = []
        for i in x:
            district.append(i['addresses'][0]['district_name'])
        print("Els districtes de Barcelona que tenen platges son: ")
        print(set(district))

def cuantitat_platges():
    with open('opendatabcn_NP-NASIA_Platges-js.json') as x:
        y = json.load(x)
        count = 0
        for i in y:
            if i['addresses'][0]['district_name'] == 'Ciutat Vella':
                count += 1
        print("La quantitat de platges que hi ha al districte de Ciutat Vella son: ")
        print(count)

district_name()
cuantitat_platges()
