'''
Rene Tubiera Sadinas
M03
UF1 A4 Prova Practica 2
14/12/23
'''

try:
    # Demana una frase
    frase = input("Digam un nombre: ")

    # Demana una lletra
    lletra = input("Digam una lletra: ")

    # contador per la quantitat de lletres
    cont_lletres = 0

    if len(lletra) == 1 and len(frase)>0:
        for i in frase:
            if i == lletra:
                cont_lletres = cont_lletres +1

        print(f"La frase {frase} te {cont_lletres} lletres {lletra}")
    else:
        print("Error: un caracter només i una frase:")
except ValueError:
    print("Error")
'''
try:
    # Demana una frase
    frase = input("Digam un nombre: ")

    # Demana una lletra
    lletra = input("Digam una lletra: ")

    # contador per la quantitat de digits
    quantitat_de_digits = 0

    # Separa la frase
    llista_lletres = frase.split()
    # Guarda les lletres que te la frase que s'ha demanat

    lletres = []
    # si llestra esta en el rang de la llista de lletra
    for lletra in llista_lletres:
        # Si la lletra esta en la llista_lletra
        if lletra.lower() in [llista_lletres]:
            # sumara 1 si la lletra esta en la frase
            quantitat_de_digits += 1
            lletres.append(lletra)

    print(f"La frase {frase} te {quantitat_de_digits} lletres {lletra}")
except ValueError:
    print("Error")


'''
try:
    # Demana una frase
    frase = input("Digam un nombre: ")

    # Demana una lletra
    lletra = input("Digam una lletra: ")

    # contador per la quantitat de lletres
    quantitat_de_lletres = 0

    # Separa la frase
    llista_lletres = list(frase)

    # si lletra esta en el rang de la llista de lletra
    lletres = []
    for lletra_frase in llista_lletres:
        # Si la lletra esta en la llista_lletra
        if lletra_frase.lower() == lletra.lower():
            # suma 1 si la lletra está en la frase
            quantitat_de_lletres += 1
            lletres.append(lletra_frase)

    print(f"La frase '{frase}' té {quantitat_de_lletres} lletres '{lletra}'")
except ValueError:
    print("Error")

'''
'''
