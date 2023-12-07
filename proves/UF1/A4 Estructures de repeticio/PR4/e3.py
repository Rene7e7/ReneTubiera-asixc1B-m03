"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
e3. Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
 Ex: 	si el límit és 31 sumaParells 240 i sumaSenars 225
si el límit és 54 sumaParells 702 i sumaSenars 729
"""
# Hecho por los dos
parell = 0
imparell = 0
try:
    num = int(input("Dime numero de limite: "))
# El par va desde 0 saltando de 2 en 2 y sumando entre ellos
    for i in range(0, num+1, 2):
        parell += i
# El impar lo mismo pero comenzando desde el 1
    for j in range(1,num+1,2):
        imparell += j
    print("Si el limit és", num, "sumaParells es ", parell, " i sumaSenar és ", imparell )
except:
    print("Error")