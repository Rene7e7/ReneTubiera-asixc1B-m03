"""
e5. isACorrectDate.py
Programa que comprovi si una data és correcte.
El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
Cal recordar que hi ha anys de traspàs.
NO es pot fer servir funcions de calendari com ara datetime de Python.
"""

dia = int(input())
mes = int(input())
any = int(input())

fecha = dia,"/",mes,"/",any
formato_fecha = "DD/MM/AA"

if fecha == formato_fecha:
    print("Este formato de fecha es correcta")
