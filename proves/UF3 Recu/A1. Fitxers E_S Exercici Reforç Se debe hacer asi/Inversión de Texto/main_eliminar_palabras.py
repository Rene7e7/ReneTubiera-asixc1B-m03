from eliminar_palabras import eliminar_palabras

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'texto_sin_palabra.txt'
    palabra = 'Python'
    eliminar_palabras(archivo_entrada, archivo_salida, palabra)
    print(f"Se ha eliminado la palabra '{palabra}' del archivo '{archivo_entrada}'. El resultado se ha guardado en '{archivo_salida}'.")

if __name__ == "__main__":
    main()
