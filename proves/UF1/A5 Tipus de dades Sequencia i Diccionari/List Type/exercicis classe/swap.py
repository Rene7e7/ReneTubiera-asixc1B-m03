'''
Rene Tubiera
UF1 A5
ASIX1Bc
17/01/2024
DNI cALCULATOR
'''
try:
    lista = []
    xurro = input("Ingresa una cadena de números: ")
    lista1 = xurro.split()

    # Ahora 'lista1' contendrá los números como elementos separados
    print(lista1)

    lista.append(xurro)
    if len(lista1) >= 4:
        lista1[0], lista1[3] = lista1[3], lista1[0]
        print(lista1)
    else:
        print("La lista no tiene suficientes elementos para intercambiar.")

except ValueError:
    print("Error")

