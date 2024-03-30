'''
Volem escriure una aplicació “Passatemps”, la qual permet a un usuari poder triar un joc amb el qual desafiar l’ordinador . L’aplicació oferirà al jugador els diferents jocs disponibles amb el següent menú:

1 - El “penjat”
2 - El 3 en ratlla
3 - Buscamines
4 - Enfonsar la flota
5 - Sortir de l’aplicació

Cada opció porta a l’execució del joc corresponent. Feu el disseny modular de l’aplicació. Dins de cada mòdul, feu el disseny descendent en funcions.

Nota: poden haver-hi més mòduls que jocs, ja que hi poden haver funcionalitats que es facin servir a més d’un mòdul (o joc) i que per tant, tingui sentit ficat en un mòdul específic.

Funcionalitat mínima a implementar:
implementació de qualsevol dels 4 jocs

'''
from el_penjat import jugar_penjat
from el_3_en_ratlla import jugar_tic_tac_toe
from Buscamines import jugar_buscamines
from Enfonsar_la_flota import jugar_hundir_la_flota

# main.py
def mostrar_menu():
    print("Menú:")
    print("1 - El 'Penjat'")
    print("2 - El 3 en ratlla")
    print("3 - Buscamines")
    print("4 - Enfonsar la flota")
    print("5 - Sortir de l'aplicació")

def main():
    while True:
        mostrar_menu()
        opcio = input("Selecciona una opció (1-5): ")

        if opcio == '1':
            jugar_penjat()
        elif opcio == '2':
            jugar_tic_tac_toe()
        elif opcio == '3':
            jugar_buscamines()
        elif opcio == '4':
            jugar_hundir_la_flota()
        elif opcio == '5':
            print("Gràcies per jugar! Fins aviat.")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció correcta.")

if __name__ == "__main__":
    main()
