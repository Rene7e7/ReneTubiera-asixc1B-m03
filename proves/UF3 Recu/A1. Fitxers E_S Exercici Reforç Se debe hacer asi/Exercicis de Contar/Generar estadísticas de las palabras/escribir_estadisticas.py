# escribir_estadisticas.py
def escribir_estadisticas(archivo_salida, estadisticas):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for clave, valor in estadisticas.items():
                archivo.write(f"{clave.replace('_', ' ').capitalize()}: {valor}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
