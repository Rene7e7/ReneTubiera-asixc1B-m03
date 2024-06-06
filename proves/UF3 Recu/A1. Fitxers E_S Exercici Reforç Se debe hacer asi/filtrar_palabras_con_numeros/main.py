from leer_archivo import leer_archivo
from filtrar_palabras_con_numeros import filtrar_palabras_con_numeros
from escribir_palabras import escribir_palabras

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'palabras_con_numeros.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    palabras_con_numeros = filtrar_palabras_con_numeros(palabras)
    escribir_palabras(archivo_salida, palabras_con_numeros)

    print("Proceso completado. Las palabras que contienen números se han guardado correctamente.")

if __name__ == "__main__":
    main()
