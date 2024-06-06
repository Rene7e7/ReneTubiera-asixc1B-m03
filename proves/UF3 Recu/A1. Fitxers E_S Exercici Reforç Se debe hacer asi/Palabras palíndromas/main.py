from leer_archivo import leer_archivo
from filtrar_palabras_palindromas import filtrar_palabras_palindromas
from escribir_palabras import escribir_palabras

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'palabras_palindromas.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    palabras_palindromas = filtrar_palabras_palindromas(palabras)
    escribir_palabras(archivo_salida, palabras_palindromas)

    print("Proceso completado. Las palabras palíndromas se han guardado correctamente.")

if __name__ == "__main__":
    main()
