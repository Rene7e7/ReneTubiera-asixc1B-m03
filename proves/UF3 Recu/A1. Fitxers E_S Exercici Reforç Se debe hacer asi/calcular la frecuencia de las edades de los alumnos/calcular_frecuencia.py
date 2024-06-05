# Collection lo que hace es contar las veces que se repite un elemento en una lista.
# En este caso, se usa para contar las veces que se repite una edad en la lista de edades.
from collections import Counter

def calcular_frecuencia(edades):
    # Contar la frecuencia de las edades
    frecuencia = Counter(edades)
    # Retornar la frecuencia
    return frecuencia
