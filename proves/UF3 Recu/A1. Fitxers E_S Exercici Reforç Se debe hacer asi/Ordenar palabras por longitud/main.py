# main.py
from leer_archivo import leer_archivo
from ordenar_palabras import ordenar_palabras
from escribir_palabras import escribir_palabras

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'palabras_ordenadas.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    palabras_ordenadas = ordenar_palabras(palabras)
    escribir_palabras(archivo_salida, palabras_ordenadas)

    print("Proceso completado. Las palabras ordenadas por longitud se han guardado correctamente.")

if __name__ == "__main__":
    main()
