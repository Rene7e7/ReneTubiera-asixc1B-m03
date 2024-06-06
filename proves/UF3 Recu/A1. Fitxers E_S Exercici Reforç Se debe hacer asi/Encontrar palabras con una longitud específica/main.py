# main.py
from leer_archivo import leer_archivo
from filtrar_palabras_longitud import filtrar_palabras_longitud
from escribir_palabras import escribir_palabras

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'palabras_longitud.txt'
    longitud = 5  # Cambia esto a la longitud deseada

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    palabras_filtradas = filtrar_palabras_longitud(palabras, longitud)
    escribir_palabras(archivo_salida, palabras_filtradas)

    print("Proceso completado. Las palabras con la longitud especificada se han guardado correctamente.")

if __name__ == "__main__":
    main()
