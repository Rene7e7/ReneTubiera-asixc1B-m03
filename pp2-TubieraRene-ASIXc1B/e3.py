'''
Rene Tubiera Sadinas
M03
UF1 A4 Prova Practica 2
14/12/23
'''
# Mida de la taula de escacs
MIDA = 8
ALFIL = "x "
NEGRE = "N "
BLANC = "B "
try:
    # Fila
    fila = int(input("f? "))
    columna = int(input("c? "))
    if fila >=1 and fila <=8 and columna>=1 and columna<=8:
        for i in range(MIDA):
            # Altura
            for j in range(MIDA):
                if (columna + (fila - j) == i  or fila + (columna - i) == j or columna - (fila - j) == i or fila - (columna - i) == j):
                    print(ALFIL, end=" ")
                elif (i + j) % 2 == 0:
                    print(BLANC, end=" ")
                else:
                    print(NEGRE, end=" ")


            print()
    else:
        print(f"La mida es {MIDA}")

except ValueError:
    print("Error")


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
'''