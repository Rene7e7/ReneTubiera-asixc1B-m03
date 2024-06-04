import lectura
import quantitat_vocals as qv
import escritura

def procesar_archivo(ruta_archivo, archivo_salida):
    lineas = lectura.leer_archivo(ruta_archivo)
    # Procesar cada palabra
    for palabra in lineas:
        # Contar vocales de la palabra
        palabra = palabra.strip()
        # Calcular cantidad de vocales ( qv es el alias de quantitat_vocals )
        cantidad_vocales = qv.contar_vocales(palabra)
        qv.escribir_resultado(archivo_salida, palabra, cantidad_vocales)

def main():
    ruta_archivo = 'paraules.txt'
    archivo_salida = 'ParaulesQuantitatVocals.txt'
    procesar_archivo(ruta_archivo, archivo_salida)
    print("Se ha procesado el archivo correctamente.")

if __name__ == "__main__":
    main()
