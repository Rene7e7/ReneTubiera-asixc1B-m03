# main.py
from leer_archivo import leer_archivo
from calcular_frecuencia_letras import calcular_frecuencia_letras
from escribir_frecuencia import escribir_frecuencia

def main():
    archivo_entrada = 'paraules.txt'
    archivo_salida = 'frecuencia_letras.txt'

    palabras = leer_archivo(archivo_entrada)
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    frecuencias = calcular_frecuencia_letras(palabras)
    escribir_frecuencia(archivo_salida, frecuencias)

    print("Proceso completado. La frecuencia de letras se ha guardado correctamente.")

if __name__ == "__main__":
    main()
