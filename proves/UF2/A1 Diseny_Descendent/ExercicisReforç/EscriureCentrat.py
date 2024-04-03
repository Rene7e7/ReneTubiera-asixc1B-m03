'''
Crea una funció escriureCentrat, que rebi com a paràmetre un text i una amplada de pantalla. La funció aleshores ha d’escriure el text centrat en pantalla, tenint en compte el paràmetre que indica l’amplada d’aquesta.
Pista: hauràs d'escriure ampladaPantalla/2  - (longitud del text)/2 espais abans del text, on “ampladaPantalla” és el paràmetre que indica l’amplada de la pantalla. Si aquest paràmetre val, per exemple, 80, aleshores el text s’haurà d’escriure amb 80/2=40 caràcters davant del text.
A més, la funció ha de subratllar el missatge utilitzant el caràcter =.
Fes un programa que provi la funció. El programa ha de demanar la frase a centrar, així com la mida de l’amplada de la pantalla.

'''

def escriureCentrat(text, ampladaPantalla):
    espais = ampladaPantalla // 2 - len(text) // 2
    print("=" * ampladaPantalla)
    print(" " * espais + text)
    print("=" * ampladaPantalla)

def main():
    text = input("Introdueix el text a centrar: ")
    ampladaPantalla = int(input("Introdueix l'amplada de la pantalla: "))
    escriureCentrat(text, ampladaPantalla)

if __name__ == "__main__":
    main()

