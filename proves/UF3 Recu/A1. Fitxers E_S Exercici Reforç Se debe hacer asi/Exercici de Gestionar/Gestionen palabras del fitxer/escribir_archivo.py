def escribir_archivo(archivo_salida, contenido):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
