from leer_archivo import leer_archivo
from procesar_contenido import procesar_contenido
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'entrada.txt'
    lineas = leer_archivo(archivo_entrada)

    if lineas is not None:
        resultado = procesar_contenido(lineas)
        escribir_resultado('resultats.txt', resultado)

if __name__ == "__main__":
    main()
