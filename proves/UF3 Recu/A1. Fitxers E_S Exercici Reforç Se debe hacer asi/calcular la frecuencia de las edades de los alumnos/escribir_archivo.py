def escribir_frecuencia(archivo_salida, frecuencia):
    try:
        # Escribir en el archivo de salida la frecuencia de las edades
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            # Escribe la frecuencia de las edades en el archivo.
            for edad, cantidad in frecuencia.items():
                archivo.write(f"{edad}: {cantidad}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
