'''
Fer un programa que dibuixa un avet del Canadà.

Cal demanar la mida de l'arbre. La mida inclou el tronc i les branques
'''

TRONC="🪵"
FULLA="🌿"
ARBRE="🎄"
BOLA="🔴"
ESTEL="🔸"
ESPACIO = " "
k = 0
n = int(input("Dime un numero: "))
print(ESTEL)
for i in range(1, n, 1):
    espacios = "  " * (n - i)
    asteriscos = "🌿" * (2 * i - 1)
    print(espacios + asteriscos)
print(f"🪵")
