'''
e6.py
Escriu un programa que demani un número a l'usuari un número de mes (per exemple, el 4, és a dir) El programa ha de validar que el nombre de mes sigui entre 1 i 12, si no és així ha de mostrar un missatge d'error i preguntar novament fins que l'usuari introdueixi un número de mes vàlid.
Un cop obtingueu un nombre de mes correcte, el programa mostrarà per pantalla quants dies té el mes (al nostre exemple, 30) i el nom del mes (a l'exemple, abril). Has de fer servir llistes. Per simplificar suposarem que el febrer sempre té 28 dies.

'''

# Crear un diccionario con la información sobre los meses
informacion_meses = {
    1: {"Enero": 31},
    2: {"Febrero": 28},
    3: {"Marzo": 31},
    4: {"Abril": 30},
    5: {"Mayo": 31},
    6: {"Junio": 30},
    7: {"Julio": 31},
    8: {"Agosto": 31},
    9: {"Septiembre": 30},
    10: {"Octubre": 31},
    11: {"Noviembre": 30},
    12: {"Diciembre": 31}
}

while True:
    try:
        numero_mes = int(input("Dime el numero de mes: "))
        if 1 <= numero_mes <= 12:
            mes = informacion_meses[numero_mes]
            print(mes)
        else:
            print("Error: El número de mes debe estar entre 1 y 12. Inténtalo de nuevo.")
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

