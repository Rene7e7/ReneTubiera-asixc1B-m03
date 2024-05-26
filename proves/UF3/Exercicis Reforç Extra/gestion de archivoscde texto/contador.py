import os

def contar(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            contingut = f.read()
            linies = contingut.count("\n") + 1
            paraules = len(contingut.split())
            caracters = len(contingut)
            return linies, paraules, caracters
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return 0, 0, 0

def guardar_resultats(ruta_fitxer, linies, paraules, caracters):
    nom_fitxer = os.path.splitext(os.path.basename(ruta_fitxer))[0]
    with open(f"{nom_fitxer}_resultats.txt", "w") as f:
        f.write(f"Línies: {linies}\nParaules: {paraules}\nCaràcters: {caracters}\n")
