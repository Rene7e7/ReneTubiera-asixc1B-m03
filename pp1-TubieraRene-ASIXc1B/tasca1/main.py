'''
Rene Tubiera Sadinas
M03 UF3 A1
9/5/2024
pp1-Tubiera-Rene-ASIXc1B
'''

import paraules_caracters as ffp

def main():
    # Demana la ruta del arxiu
    ruta_archivo = input("introdueix la ruta del arxiu: ")
    # Demana la longitud de la paraula
    longitud = int(input("Introduex longitud de la paraula: "))
    # Executara el programa de paraules_vocals
    ffp.palabras(ruta_archivo, longitud)
    print("S'ha creat l'arxiu correctamente.")

if __name__ == "__main__":
    main()
