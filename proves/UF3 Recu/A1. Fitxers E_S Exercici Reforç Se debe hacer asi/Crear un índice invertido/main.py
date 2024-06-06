# main.py
from leer_archivo import leer_archivo
from crear_indice_invertido import crear_indice_invertido
from escribir_indice import escribir_indice

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'indice_invertido.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    indice_invertido = crear_indice_invertido(palabras)
    escribir_indice(archivo_salida, indice_invertido)

    print("Proceso completado. El índice invertido se ha guardado correctamente.")

if __name__ == "__main__":
    main()
