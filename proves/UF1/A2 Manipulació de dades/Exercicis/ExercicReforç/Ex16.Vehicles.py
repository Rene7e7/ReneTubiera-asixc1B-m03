"""
Exercici 16
Dos vehicles A i B viatgen a velocitats vA i vB respectivament, amb vB> vA.
El vehicle B va a una distància D darrere del vehicle A.

Es demana implementar un programa que demani les velocitats dels vehicles,
expressades en km / h, i la distància entre ells (en km) Amb aquestes dades el
programa ha de calcular i mostrar el temps en minuts en què el vehicle B arribarà a l’alçada del vehicle A.

"""

VehicleA = int(input("Velocitat del vehicleA: "))
VehicleB = int(input("Velocitat del vehicleB: "))
distancia = int(input("Quants distancia tenen entre aquests 2 vehicle?: "))
temps = distancia/(VehicleA-VehicleB)

if VehicleA <= VehicleB:
    print("Mai arribara al Vehicle de davant")
else:

    print(temps/60)


print("La distancia que tenen es de: ","km")
