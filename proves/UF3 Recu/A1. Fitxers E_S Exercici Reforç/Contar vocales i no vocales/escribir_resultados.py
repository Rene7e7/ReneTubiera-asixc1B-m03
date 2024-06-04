def escribir_resultados(archivo_vocales, archivo_no_vocales, contador_vocales, contador_no_vocales):
    try:
        with open(archivo_vocales, 'w', encoding='utf-8') as archivo:
            archivo.write(f'Vocales: {contador_vocales}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_vocales}': {e}")

    try:
        with open(archivo_no_vocales, 'w', encoding='utf-8') as archivo:
            archivo.write(f'No vocales: {contador_no_vocales}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_no_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_no_vocales}': {e}")
