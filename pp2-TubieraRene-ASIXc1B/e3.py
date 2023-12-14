'''
Rene Tubiera Sadinas
M03
UF1 A4 Prova Practica 2
14/12/23
'''
try:
    # Mida de la taula de escacs
    MIDA = 8
    posicion_alfil = int(input("Digam la posicio que esta el alfil: "))
    # Fila
    for i in range(MIDA):
        # Altura
        for j in range(MIDA):
            # Si i + j es divisible a 2 printara B pero sino sera N
            if (i + j) % 2 == 0:
                casillas = "B"
            else:
                casillas = "N"
            print(casillas, end=" ")
        print()
except ValueError:
    print("Error")