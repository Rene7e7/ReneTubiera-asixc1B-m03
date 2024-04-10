# region Leer
NOM_FITXER="poble1.txt"
try:
    f = open(NOM_FITXER, mode='rt')
    r=f.read(4)
    #print(r)
    r2=f.read()
    print(r2)
    f.close()
except FileNotFoundError:
    print("Fitxer/Directory no trobat:" + NOM_FITXER)
# endregion