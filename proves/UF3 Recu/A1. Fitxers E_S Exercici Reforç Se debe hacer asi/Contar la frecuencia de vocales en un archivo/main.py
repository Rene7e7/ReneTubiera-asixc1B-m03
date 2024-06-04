from leer_archivo import leer_archivo
from contar_vocales import contar_vocales
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_vocales.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Contar la frecuencia de las vocales
        contador = contar_vocales(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, contador)

if __name__ == "__main__":
    main()
