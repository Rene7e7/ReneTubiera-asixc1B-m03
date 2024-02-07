'''
cap and cua
'''

# Obtener el número de elementos en la lista
n = int(input())

# Obtener la lista de valores del usuario
valores = list(map(int, input().split()))

# Verificar si la lista es capicúa
if valores == valores[::-1]:
    print("cap i cua")
else:
    print("no cap i cua")
