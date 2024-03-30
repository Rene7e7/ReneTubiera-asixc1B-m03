# Implementación básica del juego del Penjat en Python
# Puedes personalizar la lista de palabras

import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "juego", "computadora", "desarrollo"]
    return random.choice(palabras)

def jugar_penjat():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    letras_adivinadas = []

    while intentos > 0:
        letra = input("Ingresa una letra: ").lower()

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
        else:
            intentos -= 1

        palabra_mostrada = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
        print(f"Palabra: {palabra_mostrada}")
        print(f"Intentos restantes: {intentos}")

        if palabra_mostrada == palabra_secreta:
            print("¡Ganaste!")
            break

    if intentos == 0:
        print(f"La palabra era: {palabra_secreta}. ¡Perdiste!")

jugar_penjat()
