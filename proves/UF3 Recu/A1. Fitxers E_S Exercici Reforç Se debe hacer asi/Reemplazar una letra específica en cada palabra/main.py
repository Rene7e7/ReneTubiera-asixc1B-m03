# main.py
from leer_archivo import leer_archivo
from reemplazar_letra import reemplazar_letra
from escribir_palabras import escribir_palabras

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'palabras_reemplazadas.txt'
    letra_original = 'a'  # Cambia esto a la letra que deseas reemplazar
    letra_nueva = 'o'     # Cambia esto a la nueva letra

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    palabras_reemplazadas = reemplazar_letra(palabras, letra_original, letra_nueva)
    escribir_palabras(archivo_salida, palabras_reemplazadas)

    print("Proceso completado. Las palabras con la letra reemplazada se han guardado correctamente.")

if __name__ == "__main__":
    main()
