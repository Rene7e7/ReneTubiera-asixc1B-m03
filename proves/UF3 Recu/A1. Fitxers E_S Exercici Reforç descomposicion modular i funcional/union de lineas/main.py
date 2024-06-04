# Funciones para manipular texto y archivos

def escribir_archivo(archivo, lineas):
    """
    Escribe las líneas proporcionadas en un archivo.

    Parámetros:
    archivo (str): La ruta del archivo donde se escribirán las líneas.
    lineas (list): Una lista de cadenas de texto que se escribirán en el archivo.
    """
    try:
        with open(archivo, 'w') as f:
            for linea in lineas:
                f.write(linea)
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo}': {e}")

def leer_archivo(archivo):
    """
    Lee el contenido de un archivo y lo devuelve como una lista de líneas.

    Parámetros:
    archivo (str): La ruta del archivo a leer.

    Retorna:
    list: Una lista de cadenas de texto, cada una representando una línea del archivo.
    """
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
        return lineas
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo}': {e}")
        return None

# Función para unir todas las líneas en un solo archivo

def unir_lineas(archivo_entrada, archivo_salida):
    """
    Une todas las líneas de un archivo de entrada y las guarda en un archivo de salida.

    Parámetros:
    archivo_entrada (str): La ruta del archivo de entrada.
    archivo_salida (str): La ruta del archivo de salida donde se guardará el contenido unido.
    """
    lineas = leer_archivo(archivo_entrada)
    if lineas is None:
        return
    contenido_unido = ' '.join(lineas)
    escribir_archivo(archivo_salida, [contenido_unido])

# Punto de entrada del programa

def main():
    archivo_entrada = 'texto.txt'
    archivo_salida = 'texto_unido.txt'
    unir_lineas(archivo_entrada, archivo_salida)
    print(f"Todas las líneas del archivo '{archivo_entrada}' se han unido y guardado en '{archivo_salida}'.")

if __name__ == "__main__":
    main()
