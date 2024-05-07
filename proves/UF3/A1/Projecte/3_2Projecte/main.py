import os
from paraules_boges import processar_arxiu

def main():
    directori_entrada = "./entrada"
    directori_sortida = "./sortida"
    directori_log = "./log"

    # Comprovar si els directoris de sortida i log existeixen, si no, crear-los
    for directori in [directori_entrada, directori_sortida, directori_log]:
        if not os.path.exists(directori):
            os.makedirs(directori)

    # Processar tots els arxius amb extensió .txt del directori d'entrada
    arxius_entrada = [f for f in os.listdir(directori_entrada) if f.endswith(".txt")]
    for arxiu in arxius_entrada:
        nom_arxiu = os.path.join(directori_entrada, arxiu)
        processar_arxiu(nom_arxiu)

if __name__ == "__main__":
    main()
