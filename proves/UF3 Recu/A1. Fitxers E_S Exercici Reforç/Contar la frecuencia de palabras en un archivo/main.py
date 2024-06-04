from leer_archivo import leer_archivo
from contar_palabras import contar_palabras
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'palabras.txt'
    archivo_salida = 'resultado_palabras.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Contar la frecuencia de las palabras
        contador = contar_palabras(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, contador)

if __name__ == "__main__":
    main()
