'''
Fer un programa que dibuixa un avet del Canadà.

Cal demanar la mida de l'arbre. La mida inclou el tronc i les branques
'''

# Constantes
TRONC= "🪵"

FULLA="🌿"
ARBRE="🎄"
BOLA="🔴"
ESTEL="🔸"

# Solicitar la altura al usuario
try:
    mida = int(input("Introduce la altura del árbol: "))

    # Estrella en la punta del árbol
    print("  " * (mida - 1) + ESTEL)
     # Adorno en la copa del árbol
    print("  " * (mida - 1) + BOLA)

    # Dibujo del árbol
    for i in range(1, mida + 1):
        espacios = mida - i
        hojas = 2 * i - 1
        print("  " * espacios + FULLA * hojas)

    # Dibujo del tronco
    for _ in range(mida // 3):
        print("  " * (mida - 1) + TRONC)

except ValueError:
    print("Debes ingresar un número entero.")
