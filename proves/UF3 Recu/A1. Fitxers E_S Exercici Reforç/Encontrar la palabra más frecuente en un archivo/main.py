from leer_archivo import leer_archivo
from encontrar_palabra_mas_frecuente import encontrar_palabra_mas_frecuente
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_palabra_mas_frecuente.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Encontrar la palabra más frecuente
        palabra_mas_frecuente, frecuencia = encontrar_palabra_mas_frecuente(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, f'La palabra más frecuente es: "{palabra_mas_frecuente}" con {frecuencia} apariciones')

if __name__ == "__main__":
    main()
