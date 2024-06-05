from escribir_resultado import escribir_resultado
from leer_archivo import leer_archivo
from procesar_contenido import procesar_contenido

def main():
    archivo_entrada = 'entrada.txt'
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        palabras, numeros, caracteres_especiales = procesar_contenido(contenido)

        escribir_resultado('palabras.txt', palabras)
        escribir_resultado('numeros.txt', numeros)
        escribir_resultado('caracteres_especiales.txt', caracteres_especiales)

if __name__ == "__main__":
    main()
