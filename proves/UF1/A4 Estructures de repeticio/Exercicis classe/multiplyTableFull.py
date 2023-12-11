numero_x = int(input("Dime numero: "))
# el primer bucle itera sobre los numeros del 1 al 9
# i estas iteraciones se assignan con la variable i
for i in range(1,10):
    print()
    # Dentro de este, hay otro bucle for que itera sobre los numeros del 1 al 9
    # i estas iteraciones se assignan a la varible j
    for j in range(1, 10):
        ''' En cada iteracion del bucle interior se imprime el producto j*i formateando como cadena 
        i utilizando la f-string el :2 en el formato indica que se debe reservar un espacio de ancho 2 
        para imprimir el resultado 
        el parametro end="" en la funcion d eprint se utiliza para evitar que se imprima una nueva linea desdpues de cada producto,
        assegurando que los productos se impriman en la misma linea         
         '''
        print(f"{j*i:2}", end="")
