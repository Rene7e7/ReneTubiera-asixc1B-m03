from leer_archivo import leer_archivo
from procesar_datos import dividir_palabras
from contar_palabras import contar_palabras_unicas

def main(archivo):
    contenido = leer_archivo(archivo)
    if contenido:
        palabras = dividir_palabras(contenido)
        cantidad_palabras_unicas = contar_palabras_unicas(palabras)
        if cantidad_palabras_unicas is not None:
            print(f"La cantidad de palabras únicas en el archivo '{archivo}' es: {cantidad_palabras_unicas}")

if __name__ == "__main__":
    archivo = "texto.txt"  # Reemplaza "texto.txt" por el nombre de tu archivo
    main(archivo)
