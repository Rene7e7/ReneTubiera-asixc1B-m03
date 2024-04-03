# app.py

import lectura
import classificacio

def main():
    resultatsLliga = lectura.llegirPartitsDeTeclat()
    classificacio.impClassificacio(resultatsLliga)

if __name__ == "__main__":
    main()
