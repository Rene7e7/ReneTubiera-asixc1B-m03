import procesar_archivo_palabras

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_palabras.txt'
    numero_palabras = procesar_archivo_palabras.procesar_archivo(archivo_salida)
    if numero_palabras is not None:
        print(f"El archivo contiene {numero_palabras} palabras. El resultado se ha guardado en {archivo_salida}.")

if __name__ == "__main__":
    main()
