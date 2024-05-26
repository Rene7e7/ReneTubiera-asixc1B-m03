from marcador import calcular_marcador

def main():
    n = int(input("Introdueix el nombre de partits: "))
    for _ in range(n):
        historial = input("Introdueix la història del partit: ")
        resultat = calcular_marcador(historial)
        print(resultat)

if __name__ == "__main__":
    main()
