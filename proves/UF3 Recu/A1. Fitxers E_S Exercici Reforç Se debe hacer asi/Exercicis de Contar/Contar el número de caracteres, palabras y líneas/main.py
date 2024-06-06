# main.py
from leer_archivo import leer_archivo
from contar_texto import contar_caracteres, contar_palabras, contar_lineas
from escribir_informe import escribir_informe

def main():
    ruta_entrada = 'paraules.txt'
    ruta_informe = 'informe.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(ruta_entrada)
    if contenido is None:
        return

    # Contar caracteres, palabras y líneas
    conteo_caracteres = contar_caracteres(contenido)
    conteo_palabras = contar_palabras(contenido)
    conteo_lineas = contar_lineas(contenido)

    # Escribir el informe de resultados
    escribir_informe(ruta_informe, conteo_caracteres, conteo_palabras, conteo_lineas)
    print(f"El informe ha sido escrito en {ruta_informe}")

if __name__ == "__main__":
    main()
