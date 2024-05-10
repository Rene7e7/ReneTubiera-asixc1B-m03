'''
Rene Tubiera Sadinas
M03 UF3 A1
9/5/2024
pp1-Tubiera-Rene-ASIXc1B
'''

import quantitat_vocals as ffp

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    ffp.separar_llista_lletres(ruta_archivo)
    print("S'ha afegit l'arxiu correctamente.")

if __name__ == "__main__":
    main()