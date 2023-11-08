"""
Exercici 17
Un ciclista triga T segons a recórrer el trajecte de la ciutat “A” a la ciutat “B”. El ciclista va partir de la ciutat “A” a les HH hores, MM minuts i SS segons.

Escriu un programa que calculi l'hora d'arribada a la ciutat B. Els segons en què el ciclista tarda a realitzar el trajecte i l'hora, minuts i segons de partida es demanaran per teclat.

"""

# Pedir al usuario los segundos que tarda el ciclista en realizar el recorrido
segundos_recorrido = int(input("Introduce los segundos que tarda el ciclista en realizar el recorrido: "))

# Pedir al usuario la hora de partida
hora_partida = int(input("Introduce la hora de partida (HH): "))
minutos_partida = int(input("Introduce los minutos de partida (MM): "))
segundos_partida = int(input("Introduce los segundos de partida (SS): "))

# Calcular la hora de llegada
segundos_totales_partida = hora_partida * 3600 + minutos_partida * 60 + segundos_partida
segundos_totales_llegada = segundos_totales_partida + segundos_recorrido

hora_llegada = segundos_totales_llegada // 3600
minutos_llegada = (segundos_totales_llegada % 3600) // 60
segundos_llegada = segundos_totales_llegada % 60

# Mostrar la hora de llegada
print(f"La hora de llegada a la ciudad B es: {hora_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}")


