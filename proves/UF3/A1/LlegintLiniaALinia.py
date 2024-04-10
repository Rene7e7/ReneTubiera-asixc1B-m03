def llegirFitxer(rutaFitxer):
    contingut = ""
    fitxerDeText = open(rutaFitxer, mode='r', encoding='utf-8')
    linia = fitxerDeText.readlines()
    contingut += linia
    while linia != '':
        linia = fitxerDeText.readline()
        contingut += linia

    fitxerDeText.close()
    return contingut

# main
rutaAlFitxer = input("Entra la ruta al fitxer: ")
contingutDelFitxer = llegirFitxer(rutaAlFitxer)
print(contingutDelFitxer)