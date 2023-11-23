CAP= "....\...../...."
ULLS= "...╚⊙ ⊙╝..."
COS = "═(███)═"
CUA =  " ═V═ "
mida_COS = int(input("Digam quantitat de COS: "))
print(CAP)
print(ULLS)
print(" "+COS)
if mida_COS < 5:
    print()
else:
    print(CAP)
    print(f" {ULLS}")
    for i in range(mida_COS - 3):
        print(" " + COS)
print()
print("  "+CUA)