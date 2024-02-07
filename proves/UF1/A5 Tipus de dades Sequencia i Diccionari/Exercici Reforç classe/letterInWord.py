'''
Donada una paraula i un valor indica quina lletra hi ha a la posició indicada

Els strings funcionen com si fossin llistes de chars
'''

# Llegir la paraula i la posició
paraula, posicio = input().split()

# Convertir la posició a un nombre enter
posicio = int(posicio)

# Imprimir la lletra a la posició indicada
print(paraula[posicio])
