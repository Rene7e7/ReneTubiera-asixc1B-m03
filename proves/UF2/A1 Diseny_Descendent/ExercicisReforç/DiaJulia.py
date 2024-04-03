'''
El dia julià corresponent a una data és un nombre sencer que indica els dies que han transcorregut des de l'1 de gener
de l'any donat. Volem crear un programa principal que en introduir una data (dia, mes i any) ens digui el dia julià que correspon.
Per això implementeu les següents funcions:
llegirData: Ens permet llegir per teclat una data (dia, mes i any).
diesDelMes: Rep un mes i un any i ens diu els dies d'aquell mes aquell any.
esAnyDeTraspas: Rep un any i ens diu si és de traspàs.
calcularDiaJulia: rep una data i ens torna el dia julià.
'''

def llegirData():
    dia = int(input("Introdueix el dia: "))
    mes = int(input("Introdueix el mes: "))
    any = int(input("Introdueix l'any: "))
    return dia, mes, any

def diesDelMes(mes, any):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        if esAnyDeTraspas(any):
            return 29
        else:
            return 28

def esAnyDeTraspas(any):
    return any % 4 == 0 and (any % 100 != 0 or any % 400 == 0)

def calcularDiaJulia(dia, mes, any):
    julià = dia
    for m in range(1, mes):
        julià += diesDelMes(m, any)
    return julià

def main():
    dia, mes, any = llegirData()
    print(f"El dia julià és {calcularDiaJulia(dia, mes, any)}")

if __name__ == "__main__":
    main()

'''
Millorarem l'exercici 11 fent una funció per validar la data. De manera que en llegir una data s'assegura que és vàlida.

def llegirData():
    while True:
        dia = int(input("Introdueix el dia: "))
        mes = int(input("Introdueix el mes: "))
        any = int(input("Introdueix l'any: "))
        if validarData(dia, mes, any):
            return dia, mes, any
        else:
            print("Data incorrecta")
            
def validarData(dia, mes, any):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    else:
        if esAnyDeTraspas(any):
            return dia <= 29
        else:
            return dia <= 28
            
def main():
    dia, mes, any = llegirData()
    print(f"El dia julià és {calcularDiaJulia(dia, mes, any)}")

if __name__ == "__main__":
    main()
    
'''


