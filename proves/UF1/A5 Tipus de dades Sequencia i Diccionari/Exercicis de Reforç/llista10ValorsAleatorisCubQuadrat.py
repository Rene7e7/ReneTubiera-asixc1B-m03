'''
e1.py
Realitzar un programa que inicialitza una llista amb 10 valors aleatoris
(de l'1 al 10) i posteriorment mostri en pantalla cada nombre de la llista
juntament amb el seu quadrat i el seu cub.

'''
try:
    import random
    for i in range (10):
        num = random.randint(1,10)
        num_cub = num ** 3
        num_qua = num ** 2
        print(f"El cubico de {num} es {num_cub}")
        print(f"El quadrat de {num} es {num_qua}" )

except ValueError:
    print("Error")
