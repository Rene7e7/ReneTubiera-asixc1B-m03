"""
Exercici 10
En un institut la nota de l'assignatura de Programació es calcula de la següent manera:

     • 55% de la mitjana de tres qualificacions parcials.
     • 30% de la nota d’una prova final.
     • 15% de la nota d’un treball final.

Implementa un programa que calculi la nota final a partir dels valors entrats per teclat corresponents a les qualificacions parcials i notes de la prova i treball finals.

"""

QParcials1 = int(input("Dimel a primera nota parcial: "))
QParcials2 = int(input("Dimel a segona nota parcial: "))
QParcials3 = int(input("Dimel a tercera nota parcial: "))

MJT = (QParcials1+QParcials2+QParcials3)/3
MJT55 = MJT * 0.55

PF = int(input("dime la nota final: "))
PF30 = PF * 0.3

TF = int(input("dime la treball final: "))
TF15 = PF * 0.15

NotaFinal = MJT55 + PF30 + TF15
print(TF)
print(MJT)
print(TF15)
print(NotaFinal)