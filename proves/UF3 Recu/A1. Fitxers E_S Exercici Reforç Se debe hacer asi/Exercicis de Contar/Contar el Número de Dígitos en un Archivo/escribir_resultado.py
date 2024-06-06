def escribir_resultado(archivo_salida, resultado):
    try:
        # Lo que fa es obrir el fitxer en mode escriptura
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            # recorre el diccionari i escriu en el fitxer
            archivo.write(f"El archivo contiene {resultado} dígitos.\n")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
