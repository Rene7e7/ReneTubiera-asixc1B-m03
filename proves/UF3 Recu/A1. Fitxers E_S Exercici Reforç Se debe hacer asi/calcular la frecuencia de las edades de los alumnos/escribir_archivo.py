def escribir_frecuencia(archivo_salida, frecuencia):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for edad, cantidad in frecuencia.items():
                archivo.write(f"{edad}: {cantidad}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
