def eliminar_palabras(archivo_entrada, archivo_salida, palabra):
    contenido = leer_archivo(archivo_entrada)
    if contenido is not None:
        # Se utiliza 'split' y 'join' para evitar reemplazar subcadenas dentro de otras palabras
        contenido_modificado = ' '.join(p.replace(palabra, '') for p in contenido.split())
        escribir_archivo(archivo_salida, contenido_modificado)

def escribir_archivo(archivo, contenido):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:  # Se especifica la codificación para evitar problemas con caracteres especiales
            f.write(contenido)
    except IOError as e:  # Se captura la excepción más específica relacionada con operaciones de entrada/salida
        print(f"Error al escribir en el archivo '{archivo}': {e}")

def leer_archivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:  # Se especifica la codificación para evitar problemas con caracteres especiales
            return f.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
        return None
    except IOError as e:  # Se captura la excepción más específica relacionada con operaciones de entrada/salida
        print(f"Error al leer el archivo '{archivo}': {e}")
        return None

if __name__ == "__main__":
    archivo_entrada = 'texto.txt'
    archivo_salida = 'texto_sin_palabra.txt'
    palabra = 'Python'
    eliminar_palabras(archivo_entrada, archivo_salida, palabra)
    print(f"Se ha eliminado la palabra '{palabra}' del archivo '{archivo_entrada}'. El resultado se ha guardado en '{archivo_salida}'.")
