linies = int(input("Dime nuemro por lineas"))
punts = int(input("Dime numero por puntos"))
for i in range(1, linies + 1):
    print('.' * punts)
if i < linies-1:
    print("")