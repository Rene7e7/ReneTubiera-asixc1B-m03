""""
Rene TUbiera
M03 UF1
21/09/2023
Exercici 1
"""

#Tenemos que poner la nota que hemos sacado en el examen
NotaExamen1 = int(input("Dime la nota del primer Examen: "))
NotaExamen2 = int(input("Dime la Nota del segundo Examen: "))
#Comprueba si ha aprobado los 2 examenes
if NotaExamen2 < 5 or NotaExamen1 < 5:
    print("No puedo calcular la nota final porque has suspendido algun examen ")
else:
    #Calcula la nota final
    NotaFinal = (NotaExamen2 + NotaExamen1) / 2
    print("Has Aprobado con un ", NotaFinal)
