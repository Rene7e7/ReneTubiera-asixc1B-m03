from escribir_archivo import escribir_archivo
from leer_archivo import leer_archivo
from intercambiar_mayusculas_minusculas import intercambiar_mayusculas_minusculas

def main():
    ruta_escritura = 'texto_escritura.txt'
    ruta_lectura = 'arxiu.txt'

    texto_original = 'Hola Mundo!'
    texto_intercambiado = intercambiar_mayusculas_minusculas(texto_original)
    if texto_intercambiado is None:
        return

    escribir_archivo(ruta_escritura, texto_intercambiado)

    texto_leido = leer_archivo(ruta_escritura)
    if texto_leido is None:
        return

    print("Contenido del archivo después de escribir y leer:")
    print(texto_leido)

if __name__ == "__main__":
    main()
