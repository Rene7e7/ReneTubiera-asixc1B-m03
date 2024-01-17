'''
Rene Tubiera
UF1 A5
ASIX1Bc
17/01/2024
DNI cALCULATOR
'''
try:
    WMI = ['T', 'R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    numero = int(input())
    lletra = WMI[numero%23]
    print(lletra)
except ValueError:
    print()



