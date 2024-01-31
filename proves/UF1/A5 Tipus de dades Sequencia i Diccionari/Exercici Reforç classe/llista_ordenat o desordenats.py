'''

'''

# Obtener la cantidad de enteros del usuario
n = int(input("Introdueix el nombre d'enters: "))

# Obtener la llista d'enters del usuari
llista_enteros = list(map(int, input("Introdueix els enters separats per espais: ").split()))

# Comprovar si la llista està ordenada
if all(llista_enteros[i] <= llista_enteros[i + 1] for i in range(len(llista_enteros) - 1)):
    print("ordenats")
else:
    print("desordenats")
