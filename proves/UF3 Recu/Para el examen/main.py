import procesar_archivo
import ordenar_lineas  # Importa la función de procesamiento específico

def main():
    archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    archivo_salida = input("Ingrese el nombre del archivo de salida: ")

    # Cambia 'ordenar_lineas.ordenar_lineas' por la función de procesamiento específica que necesites
    procesar_archivo.procesar_archivo(archivo_entrada, archivo_salida, ordenar_lineas.ordenar_lineas)

if __name__ == "__main__":
    main()
