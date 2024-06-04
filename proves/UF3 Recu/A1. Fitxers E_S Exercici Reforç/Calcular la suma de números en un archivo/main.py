from leer_archivo import leer_archivo
from sumar_numeros import sumar_numeros
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'numeros.txt'
    archivo_salida = 'resultado_suma.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Sumar los números
        suma_total = sumar_numeros(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, f'La suma total de los números es: {suma_total}')

if __name__ == "__main__":
    main()
