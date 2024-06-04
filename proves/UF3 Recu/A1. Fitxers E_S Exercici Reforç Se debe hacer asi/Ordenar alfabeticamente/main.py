from leer_archivo import leer_lineas
from escribir_archivo import escribir_lineas

def ordenar_lineas(archivo_entrada, archivo_salida):
    try:
        lineas = leer_lineas(archivo_entrada)
        lineas.sort()  # Ordenar las líneas alfabéticamente
        escribir_lineas(archivo_salida, lineas)
        print(f"Las líneas del archivo '{archivo_entrada}' se han ordenado alfabéticamente y guardado en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    archivo_entrada = "texto.txt"
    archivo_salida = "texto_ordenado.txt"
    ordenar_lineas(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()
