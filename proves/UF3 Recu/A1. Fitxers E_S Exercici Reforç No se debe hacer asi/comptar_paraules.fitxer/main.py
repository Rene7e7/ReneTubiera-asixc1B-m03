from lectura import llegir_arxiu
from conteo import comptar_paraules

def main():
    ruta = 'frases.txt'
    frases = llegir_arxiu(ruta)
    comptar_paraules(frases)

if __name__ == "__main__":
    main()
