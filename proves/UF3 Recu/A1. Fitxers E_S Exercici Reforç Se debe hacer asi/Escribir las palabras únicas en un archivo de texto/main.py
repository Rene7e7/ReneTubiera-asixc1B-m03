from leer_archivo import leer_archivo
from procesar_datos import dividir_palabras
from contar_palabras import contar_palabras_unicas
from escribir_resultado import escribir_palabras_unicas

def main(archivo_entrada, archivo_salida):
    contenido = leer_archivo(archivo_entrada)
    if contenido:
        palabras = dividir_palabras(contenido)
        palabras_unicas = set(palabras)
        cantidad_palabras_unicas = contar_palabras_unicas(palabras)
        if cantidad_palabras_unicas is not None:
            escribir_palabras_unicas(archivo_salida, palabras_unicas)

if __name__ == "__main__":
    archivo_entrada = "texto.txt"  # Reemplaza "texto.txt" por el nombre de tu archivo
    archivo_salida = "palabras_unicas.txt"  # Nombre del archivo de salida
    main(archivo_entrada, archivo_salida)
