'''
e9.py
Volem guardar la temperatura mínima i màxima de 5 dies i tot seguit processar aquesta informació. Per fer-ho, realitza un programa que faci el següent:
Demanar la temperatura mínima i màxima de cadascun dels 5 dies
Mostrar a continuació la temperatura mitjana de cada dia
Després, mostri els dies amb menys temperatura
Finalment, demani una temperatura per teclat i a continuació mostri els dies la temperatura màxima dels quals coincideix amb ella. Si no hi ha cap dia que coincideixi amb alguna de les temperatures màximes, cal mostrar un missatge d'error.
Nota: per desar la temperatura màxima i mínima de cada dia, se suggereix utilitzar una llista que contindrà la informació per als 5 dies on cada element de la llista serà una llista de 2 elements: la temperatura mínima i la temperatura màxima.

'''
temperaturas = []

for dia in range(1, 6):
    temp_min = int(input(f"Dime temperatura mínima del día {dia}: "))
    temp_max = int(input(f"Dime temperatura máxima del día {dia}: "))
    temperaturas.append([temp_min, temp_max])
    print(f"Las temperaturas del día {dia} son: Mínima: {temp_min}º, Máxima: {temp_max}º")

# Calcular y mostrar la temperatura promedio de cada día
for dia in range(1, 6):
    temp = temperaturas[dia - 1]
    temp_promedio = sum(temp) / len(temp)
    print(f"La temperatura promedio del día {dia} es: {temp_promedio}º")

# Mostrar los días con las temperaturas mínimas
temp_minima_global = min([temp[0] for temp in temperaturas])
dias_temp_minima = [dia for dia in range(1, 6) if temperaturas[dia - 1][0] == temp_minima_global]
print(f"Días con la temperatura mínima global ({temp_minima_global}º): {dias_temp_minima}")

# Pedir una temperatura por teclado y mostrar los días con la temperatura máxima coincidente
temp_buscada = int(input("Dime una temperatura para buscar los días con la temperatura máxima coincidente: "))
dias_temp_buscada = [dia for dia in range(1, 6) if temperaturas[dia - 1][1] == temp_buscada]

if dias_temp_buscada:
    print(f"Días con la temperatura máxima coincidente ({temp_buscada}º): {dias_temp_buscada}")
else:
    print("No hay días con la temperatura máxima coincidente.")



