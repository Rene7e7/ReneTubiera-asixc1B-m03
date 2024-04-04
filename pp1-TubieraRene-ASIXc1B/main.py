from Utilitat1 import Utilitat1
from Utilitat2 import Utilitat2
from Utilitat3_1 import Utilitat3_1
from Utilitat3_2 import Utilitat3_2
from Utilitat4 import Utilitat4
def menu_principal():
    try:
        while True:
            print("\nMenú principal:")
            print("1 - signes puntuacio - Quantitat")
            print("2 - Signes puntuació ")
            print("3 Text - Codificar ")
            print("4 Text - Codificar ")
            print("5 - Executar totes les Utilitats ")
            print("6 - Sortir de l’aplicació")

            opcion = input("Selecciona una opció: ")

            if opcion == "1":
                Utilitat1()
            elif opcion == "2":
                Utilitat2()
            elif opcion == "3":
                Utilitat3_1()
            elif opcion == "4":
                Utilitat3_2()
            elif opcion == "5":
                Utilitat1()
                Utilitat2()
                Utilitat3_1()
                Utilitat3_2()
                Utilitat4()
            elif opcion == "6":
                print("Adéu!")
                break
            else:
                print("Opció no vàlida, si us plau, tria una opció vàlida.")
    except ValueError:
        print("Error")
if __name__ == "__main__":
    menu_principal()

