# programa_principal.py

from leer_datos import leer_datos
from procesar_datos import calcular_total_ventas, calcular_promedio_ventas
from escribir_resultados import escribir_resultados

def main():
    archivo_entrada = "ventas.txt"
    archivo_salida = "resultados.txt"

    # Leer los datos de ventas desde el archivo
    datos = leer_datos(archivo_entrada)

    if datos:
        # Procesar los datos (calcular total y promedio de ventas)
        total_ventas = calcular_total_ventas(datos)
        promedio_ventas = calcular_promedio_ventas(datos)

        # Preparar los resultados
        resultados = [f"Total de ventas: {total_ventas}", f"Promedio de ventas: {promedio_ventas:.2f}"]

        # Escribir los resultados en un archivo de salida
        escribir_resultados(archivo_salida, resultados)

if __name__ == "__main__":
    main()
