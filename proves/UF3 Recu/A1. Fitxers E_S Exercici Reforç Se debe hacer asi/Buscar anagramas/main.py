# main.py
from leer_archivo import leer_archivo
from buscar_anagramas import buscar_anagramas
from escribir_anagramas import escribir_anagramas

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'anagramas.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    anagramas = buscar_anagramas(palabras)
    escribir_anagramas(archivo_salida, anagramas)

    print("Proceso completado. Los anagramas se han guardado correctamente.")

if __name__ == "__main__":
    main()
