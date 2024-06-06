# main.py
from leer_archivo import leer_archivo
from generar_estadisticas import generar_estadisticas
from escribir_estadisticas import escribir_estadisticas

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'estadisticas_palabras.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    estadisticas = generar_estadisticas(palabras)
    escribir_estadisticas(archivo_salida, estadisticas)

    print("Proceso completado. Las estadísticas de las palabras se han guardado correctamente.")

if __name__ == "__main__":
    main()
