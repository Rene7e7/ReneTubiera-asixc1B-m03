'''
Llegir el fitxer Dragon.in i crear el fitxer de sortida DragonEyesClosed.out amb el mateix contingut.
Però caldrà haver canviar prèviament els ulls del drac que al fitxer d'entrada estan oberts 0    0 , i al de sortida hauran d'estar tancats X    X  o també per uns '👁' '👁'

'''
NOM_FITXER = "Dragon.in"
def closeDragonsEyes():
    with open(NOM_FITXER, mode='rt', encoding='utf-8') as file:
        dragon = file.read()
        dragon = dragon.replace('0', 'X')
    with open('DragonEyesClosed.out', mode='wt', encoding='utf-8') as f2:
        f2.write(dragon)
closeDragonsEyes()