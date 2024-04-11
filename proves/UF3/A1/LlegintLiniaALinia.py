def llegirFitxer(rutaFitxer):
    contingut = ""
    fitxerDeText = open(rutaFitxer, mode='r', encoding='utf-8')
    linies = fitxerDeText.readlines()
    fitxerDeText.close()
    return linies

def main():
    rutaFitxer= input("Ruta fitxer: ")
    contingutDelFitxer = llegirFitxer(rutaFitxer)
    print(contingutDelFitxer)
    print(contingutDelFitxer[3])

if __name__ == "__main__":
    main()