# Funciones para manipular texto y archivos

def intercambiar_mayusculas_minusculas(texto):
    """
    Intercambia mayúsculas por minúsculas y viceversa en un texto dado.

    Parámetros:
    texto (str): El texto a modificar.

    Retorna:
    str: El texto con el intercambio realizado o None si hay un error.
    """
    try:
        return texto.swapcase()
    except Exception as e:
        print(f"Error al intercambiar mayúsculas y minúsculas: {e}")
        return None

def escribir_archivo(ruta, texto):
    """
    Escribe un texto en un archivo en la ruta especificada.

    Parámetros:
    ruta (str): La ruta del archivo a escribir.
    texto (str): El texto a escribir en el archivo.
    """
    try:
        with open(ruta, "w") as archivo:
            archivo.write(texto)
    except Exception as e:
        print(f"Error al escribir en el archivo '{ruta}': {e}")

def leer_archivo(ruta):
    """
    Lee el contenido de un archivo en la ruta especificada.

    Parámetros:
    ruta (str): La ruta del archivo a leer.

    Retorna:
    str: El contenido del archivo o None si hay un error.
    """
    try:
        with open(ruta, "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
        return None

# Función principal que utiliza las funciones anteriores

def main():
    ruta_escritura = 'texto_escritura.txt'
    texto_original = 'Hola Mundo!'
    texto_intercambiado = intercambiar_mayusculas_minusculas(texto_original)

    if texto_intercambiado:
        escribir_archivo(ruta_escritura, texto_intercambiado)
        texto_leido = leer_archivo(ruta_escritura)
        if texto_leido:
            print("Contenido del archivo después de escribir y leer:")
            print(texto_leido)
        else:
            print("No se pudo leer el archivo.")
    else:
        print("No se pudo intercambiar el texto.")

if __name__ == "__main__":
    main()
