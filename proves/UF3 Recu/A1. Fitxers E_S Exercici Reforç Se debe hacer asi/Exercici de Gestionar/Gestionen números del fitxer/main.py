from leer_archivo import leer_archivo
from escribir_resultado import escribir_resultado
from procesar_contenido import procesar_contenido

def main():
    archivo_entrada = 'entrada.txt'
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        numeros = procesar_contenido(contenido)

        escribir_resultado('numeros.txt', numeros)

if __name__ == "__main__":
    main()
