# escribir_informe.py
def escribir_informe(ruta, conteo_caracteres, conteo_palabras, conteo_lineas):
    informe = (f"Conteo de caracteres: {conteo_caracteres}\n"
               f"Conteo de palabras: {conteo_palabras}\n"
               f"Conteo de líneas: {conteo_lineas}\n")
    with open(ruta, 'w', encoding='utf-8') as file:
        file.write(informe)
