"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
e1. Programa que demana a l'usuari la introducció de 10 nombres sencers
(que també podrien ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla,
quants són positius, quants negatius i quants zero.
"""
#try y except para errores
try:
    num_positivo = 0
    num_negativo = 0
    num_zeros = 0

    # El bucle for pide al usuario que ingrese 10 números enteros
    for i in range(10):
        num_sencers = int(input("Digam numero Sencer: "))

        # Convierte el número entero a cadena para contar los dígitos
        num_string = str(num_sencers)

        # Cuenta los ceros en la cadena
        num_zeros += num_string.count('0')

        # Cuenta positivos, negativos y ceros
        if num_sencers > 0:
            num_positivo += 1
        elif num_sencers == 0:
            num_zeros += 1
        else:
            num_negativo += 1

    # Imprime la cantidad de positivos, negativos y ceros
    print("Positivos:", num_positivo)
    print("Negativos:", num_negativo)
    print("Ceros:", num_zeros)

except ValueError:
    # Captura el error ValueError que puede ocurrir si la entrada no es un número entero
    print("Error: Debes ingresar un número entero.")
