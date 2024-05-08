# region Importacions
from paraules_boges import llegir_arxiu, escriure_arxiu, aleatoritzar_parte_mitjana
from log import escriure_log
import time
# endregion
# region main
def main():
    try:
        escriure_log("Inici del programa")
        oracio = llegir_arxiu()
        if oracio:
            paraules_aleatoritzades = aleatoritzar_parte_mitjana(oracio)
            escriure_arxiu(paraules_aleatoritzades)
            escriure_log("Fi del programa.")
        else:
            escriure_log("No s'ha pogut llegir l'arxiu")
            print("No s'ha pogut llegir l'arxiu")
    except Exception as e:
        escriure_log(f"Error: {e}")
        print(f"Error: {e}")
# endregion
# region __main__

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Temps total transcorregut: {elapsed_time:.3f} segons")
    escriure_log(f"Temps total transcorregut: {elapsed_time:.3f} segons")
# endregion