def escribir_resultado(archivo_salida, resultado):
    try:
        # Escribe el resultado en el archivo de salida.
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            # Escribe el resultado en el archivo.
            archivo.write(f'{resultado}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
