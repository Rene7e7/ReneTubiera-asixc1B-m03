'''
Rene Tubiera Sadinas
1/02/2024
ASIXc1B
UF1 A5
Prova Practica 3
'''
try:
    filas = int(input("Digam numero de la fila: "))
    columna = int(input("Digam numero de la columna: "))
    # Si el algun numero de la fila o columan es menor que 0, donara error
    if columna <= 0 or filas <= 0:
        print("Error")
    # sino ens printara el matriu
    else:
        for i in range(filas):
            for j in range(columna):
                # Ens printara les vores en numero 1
                if i == 0 or i == filas - 1 or j == 0 or j == columna - 1:
                    print("1", end=" ")
                # La La resta de caselles ens printara en 0
                else:
                    print("0", end=" ")
            print()
except ValueError:
    print("Error")