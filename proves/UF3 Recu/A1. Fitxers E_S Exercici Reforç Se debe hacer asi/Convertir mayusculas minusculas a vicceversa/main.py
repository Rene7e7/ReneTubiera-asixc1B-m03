# main.py
from leer_archivo import leer_archivo
from procesar_texto import procesar_texto
from escribir_resultado import escribir_resultado

def main():
    ruta_entrada = 'paraules.txt'
    ruta_salida = 'resultado.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(ruta_entrada)
    if contenido is None:
        return

    # Procesar el texto
    contenido_procesado = procesar_texto(contenido)

    # Escribir el resultado en un nuevo archivo
    escribir_resultado(ruta_salida, contenido_procesado)
    print(f"El resultado ha sido escrito en {ruta_salida}")

if __name__ == "__main__":
    main()
