from leer_archivo import leer_archivo
from contar_numeros import contar_numeros
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'numeros.txt'
    archivo_salida = 'resultado_numeros.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Contar la frecuencia de los números
        contador = contar_numeros(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, contador)

if __name__ == "__main__":
    main()
