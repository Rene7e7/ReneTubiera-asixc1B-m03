from lectura import leer_notas
from procesamiento import generar_histograma
from escritura import escribir_histograma

def main():
    nombre_archivo = "histograma.txt"
    contenido = leer_notas(nombre_archivo)
    histograma = generar_histograma(contenido)

    if histograma is not None:
        nombre_archivo_histograma = nombre_archivo.split('.')[0] + "-Histograma.txt"
        escribir_histograma(nombre_archivo_histograma, histograma)

if __name__ == "__main__":
    main()
