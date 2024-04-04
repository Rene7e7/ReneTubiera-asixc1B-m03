"""
Rene Tubiera Sadinas
4/4/2024
M03 UF2 A1 i A2 pp1B - Prova Practica 1
ASIX1B
"""

def lletres():
    lletres=input()
    # Separa les lletres en una llista
    ''' Les lletres es separen en una llista amb split()'''
    llista_lletres = lletres.split()
    # Inicialitza una llista buida per emmagatzemar les vocals
    vocals = []
    # Itera sobre cada lletra i comprova si és una vocal
    for lletra in llista_lletres:
        if lletra.lower() in ['a', 'e', 'i', 'o', 'u']:
            vocals.append(lletra)
def caractersEspecials():
    # Llista dels caracters especials
    LISTA = [".", ",", ";", ":", "?", "!"]

def identificar_caracters_especials(paraula):
    caracters_especials = []
    for i, lletra in enumerate(paraula):
# Comanda isalnum son tots el caractes que no siguin caracters especials
        if not lletra.isalnum():
            caracters_especials.append((lletra, i))
    return caracters_especials

def Utilitat1(vocals):
    # Demana la quantitat de lletres
    quantitat = int(input("Introdueix la quantitat de lletres: "))
    # Demana les lletres separades per espais
    lletres = input("Introdueix les lletres separades per espais: ")
    # Imprimeix les vocals
    resultat = ' '.join(vocals)
    print(resultat)

Utilitat1()


'''
# Demana a l'usuari una paraula
palabra = input("Ingresa una palabra: ")
# Enumera los caracteres de la palabra i tambien remplaza los espacios i los elimina
num_letras = len(palabra.replace(" ",""))
print("La palabra tiene", num_letras, "letras.")


'''