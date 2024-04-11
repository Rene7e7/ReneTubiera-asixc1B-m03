# region Leer
NOM_FITXER="poble1.txt"
try:
    with open(NOM_FITXER, mode='rt', encoding='utf-8') as f:
        dragon = f.read()
        dragon =dragon.replace('0    0', 'X    X')
    with open('DragonEyesClosed.out', mode='wt', encoding='utf-8') as f2:
        f2.write(dragon)
    print(dragon)
except FileNotFoundError:
    print("Fitxer/Directory no trobat:" + NOM_FITXER)
# endregion
