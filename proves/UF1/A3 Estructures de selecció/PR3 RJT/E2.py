"""
Rene Tubiera
Jordi Yu
Taranpreet Kaur
8/11/2023
UF1 Pr3
e2.  areGrowingNumbers.py
Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
"""
N1 = int(input("Ponga un el primer numero: "))
N2 = int(input("Ponga un el segundo numero: "))
N3 = int(input("Ponga un el tercer numero: "))
if N1 < N2 < N3:
    print("Esta en orden")
else:
    print("No esta en orden")
