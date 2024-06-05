def escribir_resultado(archivo_salida, usuarios):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for usuario in usuarios:
                archivo.write(f'{usuario}\n')
            print("Usuarios de Gmail guardados correctamente en", archivo_salida)
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
