'''
Crea una funció “afegirEspaiACadaCaracter”, que rebi com a paràmetre un text i torna una cadena amb un espai
addicional després de cada caràcter. Per exemple, “Hola, tu” tornarà “H o l a ,  t u ”.
Escriu un programa on es faci servir aquesta funció, mostrant el resultat per pantalla.
Nota: no es pot fer servir la funció “replace” ni cap altre de manipulació de cadenes de Python.

'''
text = "Hola, tu"
def AfegirEspaiACadaCaracter(text):
    text2 = ""
    # Lo que hace es recorrer el texto y añadir un espacio después de cada carácter
    for c in text:
        text2 += c + " "
    return text2

def main():
    text = input("Introdueix un text: ")
    print(AfegirEspaiACadaCaracter(text))

if __name__ == "__main__":
    main()
