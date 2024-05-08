import random
import logging

def llegir_frase(frase_ordenada):

    return frase_ordenada.split()

def separar_paraules(paraula):

    return paraula

def mezclar_palabras(paraula):

    palabras_desordenadas = []
    for palabra in paraula:
        if len(palabra) <= 2:
            palabras_desordenadas.append(palabra)
        else:
            middle_part = list(palabra[1:-1])
            random.shuffle(middle_part)
            palabra_desordenada = palabra[0] + ''.join(middle_part) + palabra[-1]
            palabras_desordenadas.append(palabra_desordenada)
    return palabras_desordenadas

def arxiu_entrada():

    ruta = "entrada/paraules.txt"
    with open(ruta, "rt") as fitxer_entrada:
        paraules = fitxer_entrada.read()
    return paraules

def arxiu_sortida(frase_desordenada):

    ruta_sortida = "sortida/paraules_boges.txt"
    with open(ruta_sortida, "wt") as fs:
        for word in frase_desordenada:
            fs.write(word + "\n")
