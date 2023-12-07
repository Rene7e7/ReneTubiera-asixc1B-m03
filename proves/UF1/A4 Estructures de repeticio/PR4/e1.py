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
# El for pregunta 10 veces
    for i in range(10):
        num_sencers = int(input("Digam numero Sencer: "))
# Str encadena en fila
        num_string = str(num_sencers)
# Cuenta los numeros y ceros de la cadena
        num_zeros += num_string.count('0')
# Contar positivos y negativos
        if num_sencers > 0:
            num_positivo += 1
        elif num_sencers == 0:
            num_zeros +=0
        else:
            num_negativo +=1
    print("Positivos:",num_positivo)
# El print negativos resta los num_zeros por que cuenta como ceros
    print("Negativos:",num_negativo)
    print("Ceros:",num_zeros)
except:
    print("ValueError")