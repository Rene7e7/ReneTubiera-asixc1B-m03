# y a j u i l u s e j
numero = int(input("Dime un numero: "))
lletras = input("Dime letras: ")
vowels = "BCDFGHJKLMNÑPQRSTVXZWY"
for i in lletras:
    if i == vowels.lower():
        continue
    print(i, end= "")