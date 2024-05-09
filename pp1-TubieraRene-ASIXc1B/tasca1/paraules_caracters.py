'''
Rene Tubiera Sadinas
M03 UF3 A1
9/5/2024
pp1-Tubiera-Rene-ASIXc1B
'''

import os.path
def palabras(archivo, longitud):
    try:
        archivo = os.path.join(".", archivo)
        # Lo que fa es si llegir les paraules.txt i contar paraula per paraula
        with open(archivo, "r") as f:
            palabras_contador = [palabra.strip() for palabra in f if len(palabra.strip()) == longitud]
        # si la paraula te 2 caracters anira a palabras-2.txt
        if longitud == 2:
            with open("palabras-2.txt", "w") as f:
                for palabra in palabras_contador:
                    f.write(f"{palabra}\n")
        # si la paraula te 4 caracters anira a palabras-4.txt
        if longitud == 4:
            with open("palabras-4.txt", "w") as f:
                for palabra in palabras_contador:
                    f.write(f"{palabra}\n")
        # si la paraula te 6 caracters anira a palabras-6.txt
        if longitud == 6:
            with open("palabras-6.txt", "w") as f:
                for palabra in palabras_contador:
                    f.write(f"{palabra}\n")
        # si la paraula te 8 caracters anira a palabras-8.txt
        if longitud == 8:
            with open("palabras-8.txt", "w") as f:
                for palabra in palabras_contador:
                    f.write(f"{palabra}\n")
        # si la paraula te 10 caracters anira a palabras-10.txt
        if longitud == 10:
            with open("palabras-10.txt", "w") as f:
                for palabra in palabras_contador:
                    f.write(f"{palabra}\n")
    # si dona error donara el seguent missatge de error
    except FileNotFoundError:
        print("El archivo no existe.")