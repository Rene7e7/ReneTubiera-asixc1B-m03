from paraules_boges import llegir_arxiu, escriure_arxiu, aleatoritzar_parte_mitjana
from log import escriure_log

def main():
    oracio = llegir_arxiu()
    if oracio:
        paraules_aleatoritzades = aleatoritzar_parte_mitjana(oracio)
        escriure_arxiu(paraules_aleatoritzades)
        escriure_log("Inici del programa")
        escriure_log("Final del programa")
    else:
        escriure_log("Inici del programa sense fitxer d'entrada")
        escriure_log("Final del programa sense fitxer d'entrada")

if __name__ == "__main__":
    main()
