from leer_archivo import leer_archivo
from reemplazar_palabras import reemplazar_palabras
from guardar_archivo import guardar_archivo

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'texto_modificado.txt'

    palabra_a_reemplazar = input("Ingrese la palabra que desea reemplazar: ")
    palabra_de_reemplazo = input("Ingrese la palabra de reemplazo: ")

    texto_original = leer_archivo(archivo_entrada)
    if texto_original is None:
        return

    texto_modificado = reemplazar_palabras(texto_original, palabra_a_reemplazar, palabra_de_reemplazo)
    if texto_modificado is None:
        return

    guardar_archivo(archivo_salida, texto_modificado)
    print(f"Se ha realizado el reemplazo. El texto modificado se ha guardado en '{archivo_salida}'.")

if __name__ == "__main__":
    main()
