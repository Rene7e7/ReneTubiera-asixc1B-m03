'''
closeKnightsEyes
Llegir el fitxer Knights.in i crear el fitxer de sortida KnightEyesClosed.out amb el mateix contingut. Però caldrà,
haver canviat prèviament, els ulls del cavaller que al fitxer d'entrada estan oberts 0   0 , i al de sortida hauran d'estar tancats -    - o també per uns '👁' '👁'
'''


def closeKnightsEyes():
    with open('Knight.in.txt', mode='rt', encoding='utf-8') as file:
        knight = file.read()
        knight = knight.replace('0', '-')
    with open('KnightEyesClosed.out', mode='wt', encoding='utf-8') as f2:
        f2.write(knight)
closeKnightsEyes()