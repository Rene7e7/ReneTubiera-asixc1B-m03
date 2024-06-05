def escribir_palabras_unicas(archivo_salida, palabras_unicas):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            for palabra in palabras_unicas:
                f.write(f"{palabra}\n")
            print(f"Palabras únicas guardadas correctamente en '{archivo_salida}'")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
