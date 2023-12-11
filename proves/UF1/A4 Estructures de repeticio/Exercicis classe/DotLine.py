linies = int(input("Dime nuemro por lineas"))
punts = int(input("Dime numero por puntos"))

''' Hay un bucle for que itera desde 1 hasta linies. En cada itineracion se 
En cada iteracion, se imprime una linea de puntosn donde le nunero de ountos en cada linea 
es igual a punts'''
for i in range(1, linies + 1):
    print('.' * punts)
''' Despues del bucle, hay una condicion que cada linea de puntos
se imprima una linea en blanco solo si el valor actual de la i es menor que linies -1 '''
if i < linies-1:
    print("")
