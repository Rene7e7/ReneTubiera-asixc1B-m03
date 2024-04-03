'''
Crear un programa per treballar amb una pila. Una pila és una estructura de dades que ens permet desar un conjunt de variables.
La característica fonamental és que el darrer element que s'afegeix al conjunt és el primer que se'n pot treure.
Per representar una pila utilitzarem una llista de cadenes de caràcters.
Es crearan diverses funcions per treballar amb la pila:
llargadaPila: Funció que rep una pila i retorna el nombre d'elements que té.
estaBuidaPila: Funció que rep una pila i que retorna True si la pila és buida, (no té elements) o False en cas contrari.
afegeixAPila: Funció que rep una cadena de caràcters i una pila. La cadena és afegida al final de la pila, si aquesta no és plena.
 Si la pila està plena, es mostra un missatge d’error.
treureDeLaPila: Funció que rep una pila i que retorna l’últim element afegit. L’element serà esborrat de la pila. Si la pila està
buida es mostra un missatge d’error.
mostrarPila: Funció que rep una pila i que mostra en pantalla els elements de la pila, indicant quin element és el primer i quin
l’últim.
     Implementa un programa que faci servir les funcions, amb el següent menú:
Afegir element a la pila
Treure element de la pila
Longitud de la pila
Mostra pila
Sortir

'''

def llongitudPila(pila):
    return len(pila)

def estaBuidaPila(pila):
    return len(pila) == 0

def afegeixAPila(element, pila):
    pila.append(element)
    return pila

def treureDeLaPila(pila):
    if not estaBuidaPila(pila):
        return pila.pop()
    else:
        return "Error: la pila està buida"

def mostrarPila(pila):
    print(pila)

def main():
    pila = []
    while True:
        print("1. Afegir element a la pila")
        print("2. Treure element de la pila")
        print("3. Longitud de la pila")
        print("4. Mostra pila")
        print("5. Sortir")
        opcio = int(input("Escull una opció: "))
        if opcio == 1:
            element = input("Introdueix l'element: ")
            pila = afegeixAPila(element, pila)
        elif opcio == 2:
            print(treureDeLaPila(pila))
        elif opcio == 3:
            print(llongitudPila(pila))
        elif opcio == 4:
            mostrarPila(pila)
        elif opcio == 5:
            break
        else:
            print("Opció incorrecta")

if __name__ == "__main__":
    main()
    
