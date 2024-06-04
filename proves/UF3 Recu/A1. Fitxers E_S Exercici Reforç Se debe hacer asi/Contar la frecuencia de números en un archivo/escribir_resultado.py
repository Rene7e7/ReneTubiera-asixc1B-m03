def escribir_resultado(archivo_salida, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for numero, frecuencia in resultado.items():
                archivo.write(f'Número {numero}: {frecuencia} veces\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
