

import  cuiner
# region DEFinició de funcions
def mostrar_menu():

   print("1. Truita")

   print("2. Macarrons")

   print("6. Sushi")

   return input("Què vols per dinar?")

def main():

   opcio=mostrar_menu()

   match opcio:

       case "1": cuiner.ferTruita()

       case "2": cuiner.ferMacarrons()

       case "3" | "4" | "5": print("comming soon")

       case "6": cuiner.ferSushi()

       case _: print("OPCIÓ no vàlida")

# endregion



# Programa principal

main()