'''

'''


import random
lista = []
senar = []
parell = []
veces = 10
for i in range (veces):
    num = random.randint(1,20)
    lista.append(num)
    if i % 2 == 0:
        senar.append(num)
    else:
        parell.append(num)
print(lista)
print("Senars:",(senar),"=",float(sum(senar)/(veces//2)))
print("Parells:",(parell),"=",float(sum(parell)//(veces//2)))




