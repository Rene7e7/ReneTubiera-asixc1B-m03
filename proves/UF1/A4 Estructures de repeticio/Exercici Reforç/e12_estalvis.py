MES = 11
Estalvi = 0
sou_Total = 0
sou_gastat = 0
while MES != 12:
    sou_treballador = int(input(f"Quin es el teu sou del {MES} mes: "))
    estalvi_treballador = int(input(f"Digam quants diners vols estalviar el {MES} mes: "))
    Estalvi_Total = + estalvi_treballador
    print(f"En {MES} vol estalviar {Estalvi_Total}")
    print(f"El sou del {MES} mes es {sou_treballador}")
    MES += 1
    sou_Total += sou_treballador
    sou_gastat += sou_treballador - estalvi_treballador
    print(f"Total sou gastat en {MES} mes/os: {sou_gastat}")
    print("-------------------------------------------------")
print("Programa acabat")
