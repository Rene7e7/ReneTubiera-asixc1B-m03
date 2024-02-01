'''
Rene Tubiera Sadinas
1/02/2024
ASIXc1B
UF1 A5
Prova Practica 3
'''



try:
    frase = input("Digam una frase per encriptar: ")
    llista_lletras_frase = frase.split()
    frase_incriptada = []
    lletras = []
    # vocabulari
    vocabulari = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    print(llista_lletras_frase)
    print(frase_incriptada, end=":")
except ValueError:
    print("Error")