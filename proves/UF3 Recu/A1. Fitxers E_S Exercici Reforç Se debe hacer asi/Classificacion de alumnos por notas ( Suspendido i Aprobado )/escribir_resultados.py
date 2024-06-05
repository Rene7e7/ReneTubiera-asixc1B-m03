def escribir_resultados(archivo_salida, alumnos, estado):
    try:
        # Se abre el archivo de salida en modo escritura
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            # Se recorre la lista de alumnos
            for nombre, nota in alumnos:
                # Se escribe en el archivo el nombre, la nota y el estado del alumno
                archivo.write(f'{nombre}, {nota}, {estado}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
