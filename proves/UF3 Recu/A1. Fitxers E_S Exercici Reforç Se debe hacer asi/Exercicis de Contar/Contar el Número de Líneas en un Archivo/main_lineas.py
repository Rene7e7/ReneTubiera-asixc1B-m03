import procesar_archivo_lineas

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_lineas.txt'
    numero_lineas = procesar_archivo_lineas.procesar_archivo(archivo_entrada, archivo_salida)
    if numero_lineas is not None:
        print(f"El archivo contiene {numero_lineas} líneas. El resultado se ha guardado en {archivo_salida}.")

if __name__ == "__main__":
    main()
