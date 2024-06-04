from leer_archivo import leer_archivo
from contar_caracteres_especiales import contar_caracteres_especiales
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_caracteres_especiales.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Contar la frecuencia de los caracteres especiales
        contador = contar_caracteres_especiales(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, contador)

if __name__ == "__main__":
    main()
