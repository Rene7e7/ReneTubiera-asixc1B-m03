'''
Farem un programa similar al de l’exercici 14 per treballar amb una cua. Una cua és una estructura de dades que ens permet desar un conjunt de variables. La característica fonamental és que el primer element que s'afegeix al conjunt és el primer que se'n pot treure.


Per representar una cua, com en el cas de la pila, utilitzarem una llista de cadenes de caràcters.
Com a l’exercici de la pila, crearem diverses funcions per treballar en aquest cas amb la cua:
llargadaCua: Funció que rep una cua i retorna el nombre d'elements que té.
estaBuidaCua Funció que rep una cua i que retorna True si la cua és buida (no té elements) o False en cas contrari.
afegeixACua: Funció que rep una cadena de caràcters i una cadena. Si la cua no és plena, la cadena és afegida al final de la cua.
Si la cua està plena, es mostra un missatge d’error.
treureDeLaCua: Funció que rep una cua i que retorna el primer element afegit. L’element en qüestió serà esborrat de la cua.
Si la cua està buida, es mostra un missatge d’error.
mostrarCua: Funció que rep una cua  i que mostra en pantalla els elements de la cua, indicant quin element és el primer i quin l’últim.


'''

def llongitudCua(cua):
    return len(cua)

def estaBuidaCua(cua):
    return len(cua) == 0

def afegeixACua(element, cua):
    cua.append(element)
    return cua

def treureDeLaCua(cua):
    if not estaBuidaCua(cua):
        return cua.pop(0)
    else:
        return "Error: la cua està buida"

def mostrarCua(cua):
    print(cua)

def main():
    cua = []
    while True:
        print("1. Afegir element a la cua")
        print("2. Treure element de la cua")
        print("3. Longitud de la cua")
        print("4. Mostra cua")
        print("5. Sortir")
        opcio = int(input("Escull una opció: "))
        if opcio == 1:
            element = input("Introdueix l'element: ")
            cua = afegeixACua(element, cua)
        elif opcio == 2:
            print(treureDeLaCua(cua))
        elif opcio == 3:
            print(llongitudCua(cua))
        elif opcio == 4:
            mostrarCua(cua)
        elif opcio == 5:
            break
        else:
            print("Opció incorrecta")

if __name__ == "__main__":
    main()

