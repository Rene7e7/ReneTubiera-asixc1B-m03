from union_lineas import unir_lineas

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'texto_unido.txt'
    unir_lineas(archivo_entrada, archivo_salida)
    print(f"Todas las líneas del archivo '{archivo_entrada}' se han unido y guardado en '{archivo_salida}'.")

if __name__ == "__main__":
    main()
