CAP = "....\...../...."
ULLS = "...╚⊙ ⊙╝..."
COS = "═(███)═"
CUA = " ═V═ "
mida_serp = int(input("Introdueix la mida de la serp: "))
ZIGAZAGA = [1, 2, 3, 4, 3, 2]

if mida_serp < 5:
    print("La mida de la serp ha de ser com a mínim 5.")
else:
    print(CAP)
    print(f" {ULLS}")

    # Bucle que itera sobre la longitud de la serpiente (mida_serp - 3 veces)
    for i in range(mida_serp - 3):
        # Imprime espacios en blanco según el patrón definido por ZIGAZAGA
        print(" " * ZIGAZAGA[i % 6], end="")
        # Imprime la parte del cuerpo de la serpiente
        print(f" {COS}")

    # Imprime la cola de la serpiente
    print(f" {CUA}")
