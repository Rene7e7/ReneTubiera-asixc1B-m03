from UtilitatsEstadistiques import menu_estadisticas
from UtilitatsCadenes import menu_cadenas

def menu_principal():
    while True:
        print("\nMenú principal:")
        print("1 - Utilitats Estadístiques")
        print("2 - Utilitats de Cadenes")
        print("3 - Sortir de l’aplicació")

        opcion = input("Selecciona una opció: ")

        if opcion == "1":
            menu_estadisticas()
        elif opcion == "2":
            menu_cadenas()
        elif opcion == "3":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida, si us plau, tria una opció vàlida.")

if __name__ == "__main__":
    menu_principal()
