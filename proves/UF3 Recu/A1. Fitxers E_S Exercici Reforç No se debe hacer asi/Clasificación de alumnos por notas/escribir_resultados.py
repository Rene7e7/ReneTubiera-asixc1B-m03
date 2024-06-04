def escribir_resultados(archivo_salida, alumnos):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for nombre, nota in alumnos:
                archivo.write(f'{nombre}, {nota}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
