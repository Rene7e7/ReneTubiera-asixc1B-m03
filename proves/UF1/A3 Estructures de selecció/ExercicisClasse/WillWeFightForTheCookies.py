"""
Rene Tubiera
25/10/2023
UF1
M03
"""
entrada = input()
entrada = entrada.split()
persones = int(entrada[0])
galetes = int(entrada[1])

if galetes % persones == 0:
    print("Lets Eat!")
else:
    print("Lets Fight")


"""
Codi correcte
personas, galetes = input().split()
numPersonas = int(persones)
num_galetes = int(galetes)
if num_galetes % num_persones == 0:
    print("lets eat")
else:
    print("Lets Fight")
"""