def escribir_resultados(archivo_vocales, archivo_no_vocales, frecuencia_vocales, frecuencia_no_vocales):
    try:
        with open(archivo_vocales, 'w', encoding='utf-8') as archivo:
            for vocal, frecuencia in frecuencia_vocales.items():
                archivo.write(f'{vocal}: {frecuencia}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_vocales}': {e}")

    try:
        with open(archivo_no_vocales, 'w', encoding='utf-8') as archivo:
            for no_vocal, frecuencia in frecuencia_no_vocales.items():
                archivo.write(f'{no_vocal}: {frecuencia} veces\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_no_vocales}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_no_vocales}': {e}")
