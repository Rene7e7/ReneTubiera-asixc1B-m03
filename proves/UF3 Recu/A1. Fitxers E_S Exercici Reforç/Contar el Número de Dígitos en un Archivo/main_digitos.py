import procesar_archivo_digitos

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'resultado_digitos.txt'
    numero_digitos = procesar_archivo_digitos.procesar_archivo(archivo_entrada, archivo_salida)
    print(f"El archivo contiene {numero_digitos} dígitos. El resultado se ha guardado en {archivo_salida}.")

if __name__ == "__main__":
    main()
