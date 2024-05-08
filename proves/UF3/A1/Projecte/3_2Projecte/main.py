import os
from paraules_boges import processar_arxiu
from log import escriure_log
from datetime import datetime
import time
def main():

    directori_entrada = "./entrada"
    directori_sortida = "./sortida"
    directori_log = "./log"
    # con datatime
    escriure_log(f"{datetime.now()} - Inici del programa")
    # Comprovar si els directoris de sortida i log existeixen, si no, crear-los
    for directori in [directori_entrada, directori_sortida, directori_log]:
        if not os.path.exists(directori):
            os.makedirs(directori)

    # Processar tots els arxius amb extensió .txt del directori d'entrada
    arxius_entrada = [f for f in os.listdir(directori_entrada) if f.endswith(".txt")]
    for arxiu in arxius_entrada:
        nom_arxiu = os.path.join(directori_entrada, arxiu)
        processar_arxiu(nom_arxiu)
    escriure_log(f"{datetime.now()} - Fi del programa")



if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Temps total transcorregut: {elapsed_time:.3f} segons")
    escriure_log(f"Temps total transcorregut: {elapsed_time:.3f} segons")