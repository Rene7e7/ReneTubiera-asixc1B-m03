'''
e10.py
Escriure un programa que:
Crea una taula (llista amb dues dimensions) de 5x5 nombres enters
Llegeix per teclat els nombres enters per a cada casella de la taula
Mostra per pantalla la suma de tots els elements de cada fila i la suma de tots els elements de cada columna
Pista: una taula es pot veure com una llista de llistes.

'''

try:
    taula = 5
    contadorNum_fila = 0
    fila = 1
    taula_llista = [

        1, [],
        2, [],
        3, [],
        4, [],
        5, []
    ]
    for i in range(5*5):
        numero = int(input(f"Dime un numero de la fila {fila}: "))
        if numero > 0:
            contadorNum_fila += 1
            print(contadorNum_fila)
            taula_llista.append(numero)
        if contadorNum_fila == 5:
            contadorNum_fila = 0
            fila += 1



except ValueError:
    print("Error")