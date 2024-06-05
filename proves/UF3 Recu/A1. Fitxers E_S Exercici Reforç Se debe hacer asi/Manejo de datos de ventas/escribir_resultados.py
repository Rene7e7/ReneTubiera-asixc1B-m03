# escribir_resultados.py

def escribir_resultados(archivo_salida, resultados):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for resultado in resultados:
                archivo.write(f'{resultado}\n')
        print(f"Los resultados se han guardado correctamente en '{archivo_salida}'.")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
