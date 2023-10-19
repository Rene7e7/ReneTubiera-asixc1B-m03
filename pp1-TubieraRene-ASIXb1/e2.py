"""
Rene Tubiera Sadinas
19/10/23
M03
UF1
Pp1B Prova Practica
Exercici nota final de la UF1 del mòdul 03 del Cicle de Grau Superior d'Administració de Sistemes Informàtics en Xarxa (CFGS ASIX)
"""
# Demanem a l'usuari que posi les Notes de la RA1 i RA2 de cada estudiant
RA1_Estudiant1 = int(input("Donam la nota del RA1 del estudiant 1: "))
RA1_Estudiant2 = int(input("Donam la nota del RA1 del estudiant 2: "))
RA1_Estudiant3 = int(input("Donam la nota del RA1 del estudiant 3: "))
RA2_Estudiant1 = int(input("Donam la nota del RA1 del estudiant 1: "))
RA2_Estudiant2 = int(input("Donam la nota del RA1 del estudiant 2: "))
RA2_Estudiant3 = int(input("Donam la nota del RA1 del estudiant 3: "))

# Calcul de la QUF1 (QUF1 = 0,30*RA1 + 0,70*RA2) de cada estudiant
QUF1_Estudiant1 = 0.30 * RA1_Estudiant1 + 0.70 * RA2_Estudiant1
QUF1_Estudiant2 = 0.30 * RA1_Estudiant2 + 0.70 * RA2_Estudiant2
QUF1_Estudiant3 = 0.30 * RA1_Estudiant3 + 0.70 * RA2_Estudiant3

# mostra per pantalla el resultat de la Nota Final de la UF1 de cada estudiant peró en 2 decimals
print("La Nota final de la UF1 del estudiant 1 es: ", int(QUF1_Estudiant1))
print("La Nota final de la UF1 del estudiant 2 es: ", int(QUF1_Estudiant2))
print("La Nota final de la UF1 del estudiant 3 es: ", int(QUF1_Estudiant3))







