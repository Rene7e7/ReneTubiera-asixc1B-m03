def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(f"El archivo contiene {resultado} palabras.\n")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
