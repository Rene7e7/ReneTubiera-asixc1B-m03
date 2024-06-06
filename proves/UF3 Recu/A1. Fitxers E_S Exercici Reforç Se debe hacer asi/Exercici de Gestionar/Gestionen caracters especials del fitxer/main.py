from leer_archivo import leer_archivo
from procesar_contenido import procesar_contenido
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'entrada.txt'
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        caracteres_especiales = procesar_contenido(contenido)

        escribir_resultado('caracteres_especiales.txt', caracteres_especiales)

if __name__ == "__main__":
    main()
