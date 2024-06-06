# main.py
import procesar_archivo

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'paraules.txt'
    # Nombre del archivo para palabras que comienzan con la secuencia específica
    archivo_inicio = 'inicio.txt'
    # Nombre del archivo para otras palabras
    archivo_otras = 'otras.txt'
    # Secuencia específica para filtrar palabras
    inicio = 'al'  # Cambia esto a la secuencia que deseas usar

    # Llamar a la función para procesar el archivo
    procesar_archivo.procesar_archivo(archivo_entrada, archivo_inicio, archivo_otras, inicio)

    print("Proceso completado. Las palabras se han filtrado y guardado correctamente.")

if __name__ == "__main__":
    main()
