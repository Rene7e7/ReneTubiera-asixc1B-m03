from crazy_words import aleatorizar_palabras
from data_sources import get_data_from_keyboard

def main():
    oracion = get_data_from_keyboard()
    palabras_desordenadas = aleatorizar_palabras(oracion)
    imprimir_frase(palabras_desordenadas)

def imprimir_frase(palabras):
    frase = " ".join(palabras)
    print(frase.strip())

if __name__ == "__main__":
    main()
