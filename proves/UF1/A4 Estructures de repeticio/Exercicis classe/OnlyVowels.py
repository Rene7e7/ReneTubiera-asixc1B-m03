# Demana la quantitat de lletres
quantitat = int(input("Introdueix la quantitat de lletres: "))

# Demana les lletres separades per espais
lletres = input("Introdueix les lletres separades per espais: ")

# Separa les lletres en una llista
''' Les lletres es separen en una llista amb split()'''
llista_lletres = lletres.split()

# Inicialitza una llista buida per emmagatzemar les vocals
vocals = []

# Itera sobre cada lletra i comprova si és una vocal
for lletra in llista_lletres:
    if lletra.lower() in ['a', 'e', 'i', 'o', 'u']:
        vocals.append(lletra)

# Imprimeix les vocals
resultat = ' '.join(vocals)
print(resultat)
