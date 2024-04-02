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
from el_3_en_ratlla import jugar_tres_en_raya
from Buscamines import jugar_buscamines
from Enfonsar_la_flota import jugar_hundir_la_flota

def menu_principal():
    while True:
        print("\nMenú principal:")
        print("1 - El “penjat”")
        print("2 - El 3 en ratlla")
        print("3 - Buscamines")
        print("4 - Enfonsar la flota")
        print("5 - Sortir de l’aplicació")

        opcion = input("Selecciona una opció: ")

        if opcion == "1":
            jugar_penjat()
        elif opcion == "2":
            jugar_tres_en_raya()
        elif opcion == "3":
            jugar_buscamines()
        elif opcion == "4":
            jugar_hundir_la_flota()
        elif opcion == "5":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida, si us plau, tria una opció vàlida.")

if __name__ == "__main__":
    menu_principal()
