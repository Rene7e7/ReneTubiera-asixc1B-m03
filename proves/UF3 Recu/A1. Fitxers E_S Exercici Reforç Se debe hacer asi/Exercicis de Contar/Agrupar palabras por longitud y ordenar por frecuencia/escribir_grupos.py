# escribir_grupos.py
def escribir_grupos(archivo_salida, grupos):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for longitud, palabras in grupos.items():
                archivo.write(f"Longitud {longitud}:\n")
                for palabra, frecuencia in palabras:
                    archivo.write(f"  {palabra}: {frecuencia}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
