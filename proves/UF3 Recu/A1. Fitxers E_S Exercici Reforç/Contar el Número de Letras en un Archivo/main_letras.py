import procesar_archivo_letras

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_letras.txt'
    numero_letras = procesar_archivo_letras.procesar_archivo(archivo_entrada, archivo_salida)
    if numero_letras is not None:
        print(f"El archivo contiene {numero_letras} letras. El resultado se ha guardado en {archivo_salida}.")

if __name__ == "__main__":
    main()
