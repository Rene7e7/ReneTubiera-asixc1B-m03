"""
Exercici 7
Implementa un programa que llegeixi del teclat una quantitat de minuts i després mostri en pantalla a quantes hores i minuts correspon aquesta quantitat.

Per exemple: 1350 minuts són 22 hores i 30 minuts.

"""
# Pedir al usuario la cantidad de minutos
minutos = int(input("Introduce la cantidad de minutos: "))

# Calcular las horas y minutos
horas = minutos // 60
minutos_restantes = minutos % 60

# Mostrar el resultado
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
