# Posición inicial de los coches
posicion_coche1 = 70
posicion_coche2 = 150

# Solicitar la velocidad de los coches
velocidad = float(input("Introduce la velocidad de los coches en km/h: "))

# Calcular la nueva posición después de una hora
posicion_coche1 += velocidad
posicion_coche2 -= velocidad

# Mostrar la nueva posición de los coches
print(f"Después de una hora, el coche 1 se encuentra en el kilómetro {posicion_coche1}")
print(f"Después de una hora, el coche 2 se encuentra en el kilómetro {posicion_coche2}")
