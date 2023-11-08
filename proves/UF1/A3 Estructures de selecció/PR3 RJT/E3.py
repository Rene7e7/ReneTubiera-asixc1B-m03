"""
Rene Tubiera
Jordi Yu
Taranpreet Kaur
8/11/2023
UF1 Pr3
e3 fastAndFurios.py
Volem un programa que calculi la velocitat instantània i la velocitat mitjana. Cal demanar velocitat inicial (m/s), l'acceleració (m/s2) i el temps. Si la velocitat instantània és inferior o igual a 0, has d'indicar que està parat i no pots calcular la velocitat mitjana.
velocitat instantània = velocitat inicial + acceleració * temps
velocitat mitjana = (velocitat inicial + velocitat instantània )/2
"""
Inicial = int(input("Dime la velocidad inicial en (m/s): "))
Acceleracion = int(input("Dime l'acceleracion en (m/s²) "))
Temps = int(input("Dime el tiempo: "))
Instantanea = Inicial + Acceleracion * Temps

if Instantanea <= 0:
    print("Esta parado")
else:
    Mediana = (Inicial + Instantanea) / 2
    print("Esta funcionando")
