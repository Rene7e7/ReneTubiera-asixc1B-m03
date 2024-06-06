from leer_archivo import leer_archivo
from calcular_longitud_media import calcular_longitud_media
from escribir_longitud_media import escribir_longitud_media

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'longitud_media.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    longitud_media = calcular_longitud_media(palabras)
    escribir_longitud_media(archivo_salida, longitud_media)

    print("Proceso completado. La longitud media de las palabras se ha guardado correctamente.")

if __name__ == "__main__":
    main()
