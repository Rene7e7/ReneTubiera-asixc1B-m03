from leer_archivo import leer_archivo
from procesar_contenido import procesar_contenido
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'entrada.txt'
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        palabras = procesar_contenido(contenido)
        escribir_resultado('palabras.txt', palabras)

if __name__ == "__main__":
    main()
