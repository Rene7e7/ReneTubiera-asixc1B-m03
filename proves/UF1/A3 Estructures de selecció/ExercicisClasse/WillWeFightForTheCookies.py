"""
Rene Tubiera
25/10/2023
UF1
M03
"""
num_persones, num_galetes = map(int, input().split())
if num_galetes % num_persones == 0:
    print("lets eat")
else:
    print("Lets Fight")



