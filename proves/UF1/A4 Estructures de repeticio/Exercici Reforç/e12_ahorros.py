'''
e12.py
Realitzar un programa que calculi quants diners estalviarà una persona en un any,
si al final de cada mes diposita diferents quantitats de diners.
Per fer això, el programa demanarà per cada mes la quantitat que es pensa estalviar.
El programa també haurà de mostrar, a mesura que l’usuari va entrant les quantitats,
el total estalviat des del començament de l’any fins al mes per al qual s’acaba de posar la quantitat.

'''
try:
    mes = 1
    estalvi_Total = 0
    diners = 0
    print("----------------------------")
    for i in range(12):
        sou = int(input(f"Digam el teu sou del {mes} mes: "))
        quantitat_estalvi_mes = int(input(f"Digam la quantitat que vols estalviar al mes amb aquet sou {sou}: "))

        if quantitat_estalvi_mes >= 0:
            estalvi_Total += quantitat_estalvi_mes
            diners += sou - quantitat_estalvi_mes
            print("MES:",mes)
            print("sou utilitzat",sou - quantitat_estalvi_mes)
            print("Estalvi Total:",estalvi_Total)
            print("Diners gastat", diners)
            print("----------------------------")
            mes +=1

        else:
            print("Pon tu sueldo de Verdad!!!!!")
except ValueError:
    print("Solo numeros enteros")

