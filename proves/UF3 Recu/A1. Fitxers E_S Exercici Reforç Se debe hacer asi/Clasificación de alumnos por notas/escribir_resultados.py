def escribir_resultados(archivo_salida, alumnos):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            # Lo que se escribe en el archivo es una cadena de texto
            for nombre, nota in alumnos:
                # con el nombre y la nota de cada alumno separados por una coma
                archivo.write(f'{nombre}, {nota}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
