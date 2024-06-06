# escribir_anagramas.py
def escribir_anagramas(archivo_salida, anagramas):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for clave, grupo in anagramas.items():
                archivo.write(f"Anagramas de '{clave}': {', '.join(grupo)}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
