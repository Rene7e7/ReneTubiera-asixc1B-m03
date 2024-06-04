from leer_archivo import leer_archivo
from calcular_promedio import calcular_promedio
from escribir_resultado import escribir_resultado

def main():
    archivo_entrada = 'notas.txt'
    archivo_salida = 'resultado_notas.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Calcular el promedio de las notas
        promedio = calcular_promedio(contenido)

        # Escribir el resultado
        escribir_resultado(archivo_salida, f'El promedio de las notas es: {promedio}')

if __name__ == "__main__":
    main()
