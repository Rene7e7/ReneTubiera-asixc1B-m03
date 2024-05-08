import os
from paraules_boges import processar_arxiu
from log import escriure_log
import time
from datetime import date
def llegir_arxiu(nom_arxiu):

    directori_entrada = "./entrada"
    directori_sortida = "./sortida"
    directori_log = "./log"
    # con datatime
    escriure_log("Inici del programa")
    # Comprovar si els directoris de sortida i log existeixen, si no, crear-los
    for directori in [directori_entrada, directori_sortida, directori_log]:
        if not os.path.exists(directori):
            os.makedirs(directori)

    # Processar tots els arxius amb extensió .txt del directori d'entrada
    arxius_entrada = [f for f in os.listdir(directori_entrada) if f.endswith(".txt")]
    for arxiu in arxius_entrada:
        nom_arxiu = os.path.join(directori_entrada, arxiu)
        processar_arxiu(nom_arxiu)
    escriure_log("Fi del programa")


def main():
    try:
        directori_entrada = "./entrada"
        directori_sortida = "./sortida"
        directori_log = "./log"
        escriure_log("Inici del programa")
        # Comprovar si els directoris de sortida i log existeixen, si no, crear-los
        for directori in [directori_entrada, directori_sortida, directori_log]:
            if not os.path.exists(directori):
                os.makedirs(directori)

        # Processar tots els arxius amb extensió .txt del directori d'entrada
        arxius_entrada = [f for f in os.listdir(directori_entrada) if f.endswith(".txt")]
        for arxiu in arxius_entrada:
            nom_arxiu = os.path.join(directori_entrada, arxiu)
            processar_arxiu(nom_arxiu)
        escriure_log("Fi del programa")
    except Exception as e:
        escriure_log(f"Error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Temps total transcorregut: {elapsed_time:.3f} segons")
    escriure_log(f"Temps total transcorregut: {elapsed_time:.3f} segons")