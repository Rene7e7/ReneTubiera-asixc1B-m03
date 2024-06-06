# escribir_indice.py
def escribir_indice(archivo_salida, indice_invertido):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for letra, palabras in sorted(indice_invertido.items()):
                archivo.write(f"{letra}: {', '.join(sorted(palabras))}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")
