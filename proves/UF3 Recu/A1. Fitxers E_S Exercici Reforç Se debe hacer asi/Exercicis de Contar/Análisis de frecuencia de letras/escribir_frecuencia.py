# escribir_frecuencia.py
def escribir_frecuencia(archivo_salida, frecuencias):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for letra, frecuencia in frecuencias.items():
                archivo.write(f"{letra}: {frecuencia}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
