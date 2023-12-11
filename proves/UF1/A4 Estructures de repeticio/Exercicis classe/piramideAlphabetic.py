try:
    start=ord('A') # Obtiene el codigo ASCII de A
    end=ord('Z') # Obtien el codigo ASCII DE Z

    ''' El primmer bucl efor itera sobr6e los numero desde el codigo ASCII de 
    A hasta e codigo de Z '''
    for i in range(start, end + 1):
        ''' Dentro del primer bucl ehay un segundo bucle for que itera desde el codigo ASCII de A hasta el valor 
        actual de i Esto se hace paara imprimir caracteres en orden ascendente
        '''
        for j in range(start, i + 1):
            '''Dentro del segundo bucle se utiliza cht(j) para obtener el caracter
            correspondiente al codigo ASCII j se imprime este caracter seguido todos 
            los caracteres para una fila 
            i se utiliza una nueva fila utilizando print ()
            '''
            print(chr(j), end=' ')
    print()
except ValueError:
    print("Error")


"""
try:
    numero = int(input("Dime numero: "))
    letra = 65
    for i in range(1,26):
        i += 1
        for j in range(numero):
            print(chr(numero)* i)
except ValueError:
    print("Error")
"""
